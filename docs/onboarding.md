# Guide d'onboarding

## Objectifs

Ce guide permet à un nouveau membre de l'équipe de devenir opérationnel rapidement sur ce dépôt.

## Périmètre

Ce guide couvre l'installation, le workflow Git de l'équipe, le dépannage courant et les commandes utiles au quotidien.

## Dépannage

- Erreur de push refusé sur `main` : la branche est protégée, passer par une pull request.
- Conflit de merge : éditer le fichier, retirer les marqueurs `<<<<<<<`/`=======`/`>>>>>>>`, puis committer la résolution.

## Commandes utiles

- `git status` — état du dépôt
- `git log --oneline --graph --all` — visualiser l'historique
- `git rebase -i <base>` — nettoyer l'historique d'une branche avant PR


## Signature des commits

Les commits de cette equipe sont signes avec GPG (cle publique enregistree sur GitHub) afin d obtenir le badge "Verified".
