# Résolution de conflit : étape 3

## Scénario

Deux branches créées depuis le même point de départ (`main`) modifient la même ligne du même fichier, `config/app.yml` :

- `feature/increase-timeout` : `timeout_seconds: 10` devient `30` (fiabilité réseau en prod)
- `feature/reduce-timeout` : `timeout_seconds: 10` devient `5` (tests plus rapides)

## Fusion et conflit

Les deux branches ont été fusionnées l'une après l'autre dans `develop` :

```
git merge --no-ff feature/increase-timeout   # merge propre (voir note plus bas)
git merge --no-ff feature/reduce-timeout      # CONFLICT (content): Merge conflict in config/app.yml
```

Git a inséré des marqueurs de conflit (`<<<<<<<`, `=======`, `>>>>>>>`) autour de la ligne `timeout_seconds`, avec les deux valeurs concurrentes (30 vs 5).

Note : le premier merge (`feature/increase-timeout`) a lui aussi conflicté, parce que cette branche avait divergé de `main` avant le hotfix `retries` (étape 4). C'est un conflit "de voisinage" : deux lignes adjacentes modifiées chacune de leur côté. Résolu en gardant les deux changements (`timeout_seconds: 30` + `retries: 5`).

## Résolution

Choix retenu pour `timeout_seconds` : 30 secondes. La fiabilité réseau en prod prime sur la rapidité des tests ; un timeout réduit dédié pour l'environnement de test pourra être ajouté plus tard. Fichier édité à la main pour ne garder que la valeur retenue, marqueurs retirés, puis commit :

```
git add config/app.yml
git commit -m "fix: resout le conflit sur timeout_seconds (30 conserve, prime sur les erreurs reseau en prod)"
```

Vérification qu'il ne reste aucun marqueur :

```
grep -rn "<<<<<<<\|=======\|>>>>>>>" config/app.yml   # aucun résultat
```

## Différence avec l'énoncé

L'énoncé demande deux membres différents et un merge sur `main`. Le deuxième membre de l'équipe n'étant pas dispo au moment de faire cette partie, le scénario a été fait en solo et fusionné sur `develop` (pas protégée) plutôt que sur `main`, qui demande une revue d'un autre compte que l'auteur (protection mise en place à l'étape 6). L'intégration finale sur `main` se fait via une pull request classique, revue par un membre de l'équipe.
