# Atelier Git avancé & collaboratif, Séances 1, 2 et 3

![CI](https://github.com/youssouf95/esiea-devops-tp1/actions/workflows/ci.yml/badge.svg)

Dépôt pour le TP DevOps ESIEA (bloc Git avancé & collaboratif), réalisé par Youssouf Hassane ([@youssouf95](https://github.com/youssouf95)).

## Stratégie de branches : Git Flow

On est parti sur Git Flow.

### Convention de nommage

| Branche | Rôle | Créée depuis | Fusionnée dans |
|---|---|---|---|
| `main` | Code de prod, toujours stable | - | - |
| `develop` | Branche d'intégration | `main` | - |
| `feature/<sujet>` | Développement d'une fonctionnalité | `develop` | `develop` |
| `release/<x.y.z>` | Préparation d'une version | `develop` | `main` et `develop` |
| `hotfix/<sujet>` | Correctif urgent en prod | `main` | `main` et `develop` |

Exemples : `feature/hook-anti-secret`, `release/1.1.0`, `hotfix/fix-readme-typo`.

### Règle de merge

Toute fusion vers `main` ou `develop` passe par une pull request, pas de push direct. Les PR vers `main` sont fusionnées en squash merge pour garder un historique linéaire (protection de branche configurée à l'étape 6). Un fichier [`CODEOWNERS`](.github/CODEOWNERS) désigne un propriétaire par zone du dépôt ; en situation réelle d'équipe, chaque PR est revue par ce propriétaire avant merge. Les commits suivent Conventional Commits (`type(scope): description`).

## Travail réalisé pendant la séance

1. Dépôt créé, publié sur GitHub, stratégie Git Flow documentée ci-dessus.
2. Historique nettoyé par rebase interactif sur `feature/rebase-demo` (squash/reword/fixup).
3. Conflit de merge provoqué et résolu manuellement entre deux branches modifiant la même ligne, voir [docs/conflict-resolution.md](docs/conflict-resolution.md).
4. Scénario d'incident : cherry-pick d'un hotfix vers une branche de release, et `git bisect` pour isoler un commit fautif, voir [docs/bisect-demo.md](docs/bisect-demo.md).
5. Fichier `CODEOWNERS` en place (voir [docs/pr-codeowners.md](docs/pr-codeowners.md) pour le détail du cycle PR/revue/merge testé).
6. Protection avancée de `main` (PR obligatoire, revue Code Owners, historique linéaire, tags protégés), testée avec un vrai push direct refusé, voir [docs/branch-protection-test.md](docs/branch-protection-test.md).
7. Hook local `pre-commit` anti-secret (testé), commit signé GPG avec badge Verified.
8. Historique conforme à Conventional Commits, tag de release en SemVer.

## Pipeline CI (Séance 2)

Le workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) se déclenche sur chaque push vers `main` et sur chaque pull request. Il enchaîne un job `lint` (flake8) puis, seulement s'il passe (`needs: lint`), un job `test` qui lance `pytest` sur `starter-app/` en matrice sur Python 3.10, 3.11 et 3.12, avec cache des dépendances pip et rapport de couverture conservé en artefact (même en cas d'échec). Ces checks sont requis par la protection de branche sur `main` : un test cassé bloque le merge tant qu'il n'est pas corrigé (voir [docs/ci-protection-test.md](docs/ci-protection-test.md)).

### Travail réalisé pendant la séance 2

1. Application `starter-app/` intégrée, testée en local avant tout workflow (3 tests, flake8 propre).
2. Premier workflow minimal, vérifié vert dans l'onglet Actions.
3. Déclenchement sur push et pull request vérifié concrètement, `push` restreint à `main`.
4. Job `lint` séparé du job `test` (`needs: lint`), fail-fast vérifié avec une faute de style volontaire ; test ajouté pour `/status`.
5. Matrice de test sur 3 versions de Python, vérifiée dans les logs.
6. Cache pip et artefact de couverture, restauration du cache vérifiée sur un second run.
7. Statut CI obligatoire sur `main`, testé avec une PR dédiée cassant un test puis le corrigeant.
8. Badge CI ci-dessus et présente consolidation.

## Conteneurisation Docker (Séance 3)

L'image `web` (`starter-app/Dockerfile`) est un build multi-stage : un stage `builder` (`python:3.12-slim`) installe les dépendances dans un environnement isolé, un stage final (aussi `python:3.12-slim`) ne récupère que ce qui est nécessaire à l'exécution via `COPY --from=builder`, tourne en utilisateur non-root (`appuser`) et sert l'application avec `gunicorn` (pas le serveur de dev Flask).

### Gain mesuré (étape 4)

| Image | Base | Taille |
|---|---|---|
| `app-naive:1.0` (Dockerfile naïf, une seule étape) | `python:3.12` | 1.13 GB |
| `app-optim:1.0` (multi-stage) | `python:3.12-slim` | 143 MB |

Soit une réduction d'environ **87%** (image ~7,9× plus légère), mesurée avec `docker images` sur les deux images reconstruites juste avant la mesure.

### Travail réalisé pendant la séance 3

1. `starter-app/` mis à jour (ajout de `redis`/`fakeredis`), premier `Dockerfile` naïf (une étape, image `python:3.12` complète). Piège rencontré et corrigé : Flask liait `127.0.0.1` par défaut, injoignable depuis l'hôte malgré le port publié — corrigé avec `app.run(host="0.0.0.0")`.
2. Taille mesurée (`docker images`, `docker history`), utilisateur non-root ajouté (`USER appuser`, vérifié avec `docker exec ... whoami`), `.dockerignore` ajouté (contexte de build réduit de 226KB à 120B).
3. Multi-stage build (stage `builder` + stage final `slim`), remplacement du serveur de dev Flask par `gunicorn`.
4. Gain mesuré ci-dessus.

## Hooks locaux

Le dépôt fournit un hook `pre-commit` anti-secret dans [`hooks/`](hooks/). Pour l'activer localement :

```bash
git config core.hooksPath hooks
```

Il bloque un commit si le contenu stage contient un motif de secret évident (clé AWS, clé privée, `api_key = "..."`, `password = "..."`).

## Répartition des contributions

`git shortlog -sn` donne la répartition des commits par auteur.
