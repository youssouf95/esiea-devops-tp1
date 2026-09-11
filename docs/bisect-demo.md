# Scénario git bisect : étape 4

Le test `scripts/test_validate_timeout.py` a commencé à échouer quelque part dans les 7 derniers commits de `feature/bisect-demo`, sans savoir lequel.

## Recherche

```
git bisect start
git bisect bad HEAD
git bisect good 36ece2a
```

À chaque étape, `python scripts/test_validate_timeout.py` a été lancé pour juger l'état (`good` si le script affiche `OK`, `bad` sinon), pas au feeling.

## Log complet

```
git bisect start
# bad: [fe56ee3] chore(scripts): ajoute un docstring de module
git bisect bad fe56ee3
# good: [36ece2a] feat(scripts): ajoute la fonction de validation du timeout
git bisect good 36ece2a
# bad: [7abdaa8] docs(scripts): documente les parametres de la fonction
git bisect bad 7abdaa8
# bad: [85a93d9] refactor(scripts): simplifie la condition de validation
git bisect bad 85a93d9
# good: [0025035] chore(scripts): extrait les bornes de validation en constantes
git bisect good 0025035
# first bad commit: [85a93d9] refactor(scripts): simplifie la condition de validation
```

## Commit fautif

`85a93d9` (`refactor(scripts): simplifie la condition de validation`) a remplacé `MIN_TIMEOUT < seconds <= MAX_TIMEOUT` par `MIN_TIMEOUT < seconds < MAX_TIMEOUT`. Résultat : la borne max (60) était exclue par erreur.

## Correctif

Commit `fix(scripts): corrige la borne max exclue par erreur (isole via git bisect)`, qui remet le `<=`.
