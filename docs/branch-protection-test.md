# Test de la protection de branche : étape 6

Règles configurées sur `main` (via l'API GitHub) :

- Pull request obligatoire (pas de push direct), y compris pour les administrateurs (`enforce_admins: true`).
- Au moins 1 revue approuvante, avec revue obligatoire du Code Owner de la zone modifiée.
- Historique linéaire imposé (`required_linear_history: true`).
- Force-push et suppression de branche interdits.
- Tags `v*` protégés contre la suppression et le déplacement (ruleset `protection-tags-release`).

## Test réel effectué

Tentative de push direct sur `main` (administrateur du dépôt) :

```
$ git push origin main
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: - Changes must be made through a pull request.
! [remote rejected] main -> main (protected branch hook declined)
```

→ Confirmé : le push direct est bien refusé, y compris pour l'administrateur, ce qui valide que
`enforce_admins` s'applique.
