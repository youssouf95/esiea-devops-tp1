def health():
    """Renvoie l'état du service."""
    return {"status": "ok"}


if __name__ == "__main__":
    print(health())
