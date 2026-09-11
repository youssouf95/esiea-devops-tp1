# Plage acceptable pour le timeout applicatif, en secondes.
MIN_TIMEOUT = 0
MAX_TIMEOUT = 60


def validate_timeout(timeout_value):
    """
    Retourne True si le timeout est dans la plage acceptable (1 a 60 secondes).

    Args:
        timeout_value: la valeur de timeout a valider, en secondes.
    """
    return MIN_TIMEOUT < timeout_value < MAX_TIMEOUT
