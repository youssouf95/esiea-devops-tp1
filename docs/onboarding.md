# Guide d'onboarding

## Objectifs

Pour qu'un nouveau membre de l'équipe soit rapidement opérationnel sur ce dépôt.

## Périmètre

Installation, workflow Git de l'équipe, dépannage courant, commandes utiles.

## Dépannage

- Push refusé sur `main` : la branche est protégée, passer par une pull request.
- Conflit de merge : éditer le fichier, retirer les marqueurs `<<<<<<<`/`=======`/`>>>>>>>`, puis committer la résolution.

## Commandes utiles

- `git status` : état du dépôt
- `git log --oneline --graph --all` : visualiser l'historique
- `git rebase -i <base>` : nettoyer l'historique d'une branche avant PR

## Signature des commits

Les commits de l'équipe sont signés avec GPG (clé publique enregistrée sur GitHub) pour avoir le badge "Verified".

## FAQ

**Qui approuve mes PR ?**
Le propriétaire de la zone modifiée, désigné dans [`.github/CODEOWNERS`](../.github/CODEOWNERS).

**Où sont documentées les règles de branche ?**
Dans le [`README.md`](../README.md), section "Stratégie de branches".
