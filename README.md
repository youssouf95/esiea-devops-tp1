# Atelier Git avancé & collaboratif : Séance 1

Dépôt réalisé dans le cadre du TP DevOps ESIEA (bloc Git avancé & collaboratif).

## Équipe

- Youssouf Hassane ([@youssouf95](https://github.com/youssouf95))
- Romi ([@romiprobal](https://github.com/romiprobal))

## Stratégie de branches : Git Flow

Le groupe a choisi **Git Flow** comme modèle de branches.

### Convention de nommage

| Branche | Rôle | Créée depuis | Fusionnée dans |
|---|---|---|---|
| `main` | Code de production, toujours stable et déployable | - | - |
| `develop` | Branche d'intégration, contient les dernières fonctionnalités validées | `main` | - |
| `feature/<sujet>` | Développement d'une fonctionnalité | `develop` | `develop` |
| `release/<x.y.z>` | Préparation d'une version (stabilisation, derniers correctifs) | `develop` | `main` et `develop` |
| `hotfix/<sujet>` | Correctif urgent en production | `main` | `main` et `develop` |

Exemples : `feature/hook-anti-secret`, `release/1.1.0`, `hotfix/fix-readme-typo`.

### Règle de merge

- Toute fusion vers `main` ou `develop` passe par une **Pull Request**, jamais de push direct.
- Les PR vers `main` sont fusionnées en **squash merge** (un seul commit par PR) afin de conserver un **historique linéaire** sur `main`, conformément à la protection de branche configurée (voir étape 6).
- Chaque PR doit être revue et approuvée par le propriétaire désigné dans [`CODEOWNERS`](.github/CODEOWNERS) avant merge.
- Les messages de commit suivent la convention [Conventional Commits](https://www.conventionalcommits.org/) (`type(scope): description`).

## Travail réalisé pendant la séance

- **Étape 1** : Dépôt créé, publié sur GitHub, stratégie de branches Git Flow documentée ci-dessus.
- **Étape 2** : Historique nettoyé par rebase interactif sur `feature/rebase-demo` (squash/reword/fixup).
- **Étape 3** : Conflit de merge provoqué et résolu manuellement entre deux branches modifiant la même ligne (voir commit de résolution sur `main`).
- **Étape 4** : Scénario d'incident : cherry-pick d'un hotfix vers une branche de release, et `git bisect` pour isoler un commit fautif.
- **Étape 5** : Fichier `CODEOWNERS` en place, cycle PR → revue → merge réalisé.
- **Étape 6** : Protection avancée de `main` : PR obligatoire, revue Code Owners requise, historique linéaire imposé, tags de release protégés.
- **Étape 7** : Hook local `pre-commit` anti-secret, et commit signé (GPG) affichant le badge *Verified*.
- **Étape 8** : Historique conforme à Conventional Commits, tag de release en SemVer.

## Hooks locaux

Le dépôt fournit un hook `pre-commit` anti-secret dans [`hooks/`](hooks/). Pour l'activer localement :

```bash
git config core.hooksPath hooks
```

Il refuse tout commit dont le contenu stage correspond à un motif de secret évident (clé AWS, clé privée, `api_key = "..."`, `password = "..."`).

## Répartition des contributions

Voir `git shortlog -sn` pour la répartition des commits par auteur.
