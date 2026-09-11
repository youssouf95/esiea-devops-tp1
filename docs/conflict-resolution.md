# Résolution de conflit — étape 3

## Scénario

Deux branches créées à partir du même point de départ (`main`) modifient la même ligne du même
fichier, `config/app.yml` :

- `feature/increase-timeout` : `timeout_seconds: 10` → `30` (fiabilité réseau en production).
- `feature/reduce-timeout` : `timeout_seconds: 10` → `5` (accélérer les tests).

## Fusion et conflit

Les deux branches ont été fusionnées successivement dans `develop` :

```
git merge --no-ff feature/increase-timeout   # merge propre (voir note ci-dessous)
git merge --no-ff feature/reduce-timeout      # CONFLICT (content): Merge conflict in config/app.yml
```

Git a inséré des marqueurs de conflit (`<<<<<<<`, `=======`, `>>>>>>>`) autour de la ligne
`timeout_seconds`, montrant les deux valeurs concurrentes (30 vs 5).

> Note : le premier merge (`feature/increase-timeout`) a lui aussi généré un conflit, car cette
> branche avait divergé de `main` avant l'application du hotfix `retries` (étape 4) — un exemple
> concret de conflit "de voisinage" (deux lignes adjacentes modifiées chacune d'un côté). Résolu en
> conservant les deux changements (`timeout_seconds: 30` + `retries: 5`).

## Résolution

Choix retenu pour le conflit `timeout_seconds` : **30 secondes**, car la fiabilité réseau en
production prime sur la rapidité des tests ; un timeout réduit dédié pourra être introduit plus
tard spécifiquement pour l'environnement de test. Fichier édité manuellement pour ne garder que la
valeur retenue, marqueurs retirés, puis commité :

```
git add config/app.yml
git commit -m "fix: resout le conflit sur timeout_seconds (30 conserve, prime sur les erreurs reseau en prod)"
```

Vérification qu'aucun marqueur résiduel ne subsiste :

```
grep -rn "<<<<<<<\|=======\|>>>>>>>" config/app.yml   # aucun résultat
```

## Adaptation par rapport à l'énoncé

L'énoncé demande de réaliser ce scénario avec deux membres différents et de merger sur `main`.
Faute de disponibilité immédiate du deuxième membre de l'équipe, le scénario a été réalisé en
solo et fusionné sur `develop` (non protégée) plutôt que directement sur `main`, qui exige une
revue par un compte différent de l'auteur (protection configurée à l'étape 6). L'intégration finale
sur `main` se fera via une pull request standard, revue par un membre de l'équipe.
