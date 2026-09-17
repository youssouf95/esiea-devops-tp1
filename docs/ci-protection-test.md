# Statut CI obligatoire : étape 7

Une fois le pipeline CI en place (étapes 2 à 6), la protection de branche sur `main` a été mise à jour pour exiger que les checks `lint`, `test (3.10)`, `test (3.11)` et `test (3.12)` passent avant tout merge.

## Test réel effectué

Une PR dédiée ([#6](https://github.com/youssouf95/esiea-devops-tp1/pull/6)) a été ouverte avec un test volontairement cassé (`assert alert_threshold() == 999` au lieu de `25`).

Résultat :

- Les 3 jobs `test` échouent, `lint` reste vert.
- `mergeStateStatus` passe à `BLOCKED`.
- Tentative de merge via `gh pr merge` : refusée par GitHub ("the base branch policy prohibits the merge").

Le test a ensuite été corrigé (`assert alert_threshold() == 25`) et poussé sur la même PR :

- Les 4 checks repassent au vert automatiquement.
- `mergeStateStatus` repasse à `CLEAN`.
- Le merge a pu être fait sans aucune intervention manuelle sur les réglages de protection.
