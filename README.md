# Atelier Git avancé & collaboratif, Séance 1

Dépôt pour le TP DevOps ESIEA (bloc Git avancé & collaboratif).

## Équipe

- Youssouf Hassane ([@youssouf95](https://github.com/youssouf95))
- Romi Probal ([@romiprobal](https://github.com/romiprobal))

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

Toute fusion vers `main` ou `develop` passe par une pull request, pas de push direct. Les PR vers `main` sont fusionnées en squash merge pour garder un historique linéaire (protection de branche configurée à l'étape 6). Chaque PR doit être revue et approuvée par le propriétaire désigné dans [`CODEOWNERS`](.github/CODEOWNERS) avant merge. Les commits suivent Conventional Commits (`type(scope): description`).

## Travail réalisé pendant la séance

1. Dépôt créé, publié sur GitHub, stratégie Git Flow documentée ci-dessus.
2. Historique nettoyé par rebase interactif sur `feature/rebase-demo` (squash/reword/fixup).
3. Conflit de merge provoqué et résolu manuellement entre deux branches modifiant la même ligne, voir [docs/conflict-resolution.md](docs/conflict-resolution.md).
4. Scénario d'incident : cherry-pick d'un hotfix vers une branche de release, et `git bisect` pour isoler un commit fautif, voir [docs/bisect-demo.md](docs/bisect-demo.md).
5. Fichier `CODEOWNERS` en place, cycle PR/revue/merge réalisé.
6. Protection avancée de `main` (PR obligatoire, revue Code Owners, historique linéaire, tags protégés), testée avec un vrai push direct refusé, voir [docs/branch-protection-test.md](docs/branch-protection-test.md).
7. Hook local `pre-commit` anti-secret (testé), commit signé GPG avec badge Verified.
8. Historique conforme à Conventional Commits, tag de release en SemVer.

## Hooks locaux

Le dépôt fournit un hook `pre-commit` anti-secret dans [`hooks/`](hooks/). Pour l'activer localement :

```bash
git config core.hooksPath hooks
```

Il bloque un commit si le contenu stage contient un motif de secret évident (clé AWS, clé privée, `api_key = "..."`, `password = "..."`).

## Répartition des contributions

`git shortlog -sn` donne la répartition des commits par auteur.
