# Plage acceptable pour le timeout applicatif, en secondes.
MIN_TIMEOUT = 0
MAX_TIMEOUT = 60


def validate_timeout(seconds):
    """Retourne True si le timeout est dans la plage acceptable (1 a 60 secondes)."""
    return MIN_TIMEOUT < seconds < MAX_TIMEOUT
