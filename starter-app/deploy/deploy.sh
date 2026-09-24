#!/bin/bash
set -e

COMPOSE_FILE="docker-compose.deploy.yml"
PROJECT="starter-app-deploy"
STATE_FILE="deploy/active_color"

if [ -f "$STATE_FILE" ]; then
    ACTIVE=$(cat "$STATE_FILE")
else
    ACTIVE="blue"
fi

if [ "$ACTIVE" = "blue" ]; then
    IDLE="green"
    IDLE_PORT=5002
else
    IDLE="blue"
    IDLE_PORT=5001
fi

echo "Actif actuellement : $ACTIVE"
echo "Demarrage de la nouvelle version : $IDLE"

docker compose -f "$COMPOSE_FILE" -p "$PROJECT" --profile "$IDLE" up -d --build "app-$IDLE"

READY=0
for _ in $(seq 1 15); do
  if curl -sf "http://localhost:$IDLE_PORT/health" \
    > /dev/null 2>&1; then
    READY=1
    break
  fi
  sleep 2
done

if [[ "$READY" -ne 1 ]]; then
  echo "ÉCHEC : app-$IDLE ne répond pas sur /health"
  echo "ROLLBACK : arrêt de app-$IDLE, $ACTIVE reste actif"
  docker compose -f "$COMPOSE_FILE" -p "$PROJECT" --profile "$IDLE" stop "app-$IDLE"
  exit 1
fi

if ! curl -sf "http://localhost:$IDLE_PORT/status" \
  | python3 -c \
  "import sys, json; d = json.load(sys.stdin); \
  sys.exit(0 if d['deploy_color']=='$IDLE' else 1)"; then
  echo "ÉCHEC : le smoke test a échoué sur app-$IDLE"
  echo "ROLLBACK : arrêt de app-$IDLE, $ACTIVE reste actif"
  docker compose -f "$COMPOSE_FILE" -p "$PROJECT" --profile "$IDLE" stop "app-$IDLE"
  exit 1
fi

echo "Bascule du trafic vers $IDLE"
sed -i "s/app-$ACTIVE:5000/app-$IDLE:5000/" nginx/active.conf
docker compose -f "$COMPOSE_FILE" -p "$PROJECT" exec nginx nginx -s reload

echo "Arrêt de l'ancienne version : $ACTIVE"
docker compose -f "$COMPOSE_FILE" -p "$PROJECT" --profile "$ACTIVE" stop "app-$ACTIVE"

echo "$IDLE" > "$STATE_FILE"
echo "Déploiement réussi : $IDLE est maintenant actif"