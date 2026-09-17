# Pull requests et CODEOWNERS : étape 5

Le fichier [`.github/CODEOWNERS`](../.github/CODEOWNERS) assigne un propriétaire par zone du dépôt. GitHub s'en sert pour demander automatiquement une revue au propriétaire dès qu'une PR touche la zone concernée.

## Cycle PR testé

Une petite modification (ajout d'une FAQ dans `docs/onboarding.md`) a été faite sur une branche dédiée, avec une PR ouverte pour vérifier le mécanisme :

- Titre et description clairs (quoi, pourquoi) pour que le contenu se comprenne sans relire tout le diff.
- Le fichier changé touche une zone couverte par `CODEOWNERS`.
- Une revue avec commentaire de fond a été demandée avant merge, pas juste une approbation silencieuse.

## Piège vérifié

Un chemin ou un nom d'utilisateur invalide dans `CODEOWNERS` ne provoque aucune erreur visible, mais personne n'est assigné. Vérifié en ouvrant une vraie PR de test et en confirmant côté GitHub qu'un reviewer était bien demandé automatiquement.
