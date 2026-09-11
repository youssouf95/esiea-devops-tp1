# Scénario git bisect : étape 4

Un test (`scripts/test_validate_timeout.py`) a commencé à échouer quelque part dans les 7 derniers
commits de `feature/bisect-demo`, sans savoir lequel était en cause.

## Recherche

```
git bisect start
git bisect bad HEAD
git bisect good 36ece2a
```

À chaque étape, `python scripts/test_validate_timeout.py` a été exécuté pour qualifier objectivement
l'état testé (`good` si le script affiche `OK` et sort en code 0, `bad` sinon) plutôt que de deviner.

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

## Commit fautif identifié

`85a93d9` (`refactor(scripts): simplifie la condition de validation`) a remplacé
`MIN_TIMEOUT < seconds <= MAX_TIMEOUT` par `MIN_TIMEOUT < seconds < MAX_TIMEOUT`, excluant par erreur
la borne maximale (60) du domaine valide.

## Correctif

Voir le commit `fix(scripts): corrige la borne max exclue par erreur (isole via git bisect)`, qui
restaure le `<=`.
