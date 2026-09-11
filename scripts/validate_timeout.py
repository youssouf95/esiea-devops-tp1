def validate_timeout(seconds):
    """Retourne True si le timeout est dans la plage acceptable (1 a 60 secondes)."""
    return 0 < seconds <= 60
