# Test de la protection de branche : étape 6

Règles mises sur `main` (via l'API GitHub) :

- Pull request obligatoire, pas de push direct, même pour les admins (`enforce_admins: true`)
- Au moins 1 revue approuvante, revue du Code Owner de la zone modifiée obligatoire
- Historique linéaire imposé (`required_linear_history: true`)
- Force-push et suppression de branche interdits
- Tags `v*` protégés contre suppression/déplacement (ruleset `protection-tags-release`)

## Test réel

Tentative de push direct sur `main` avec le compte admin du dépôt :

```
$ git push origin main
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: - Changes must be made through a pull request.
! [remote rejected] main -> main (protected branch hook declined)
```

Le push direct est bien refusé, même pour l'admin. `enforce_admins` marche.
