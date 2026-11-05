def pozdrav(jmeno: str) -> str:
    """Vrátí pozdrav pro zadané jméno."""
    return f"Ahoj, {jmeno}!"


if __name__ == "__main__":
    print(pozdrav("světe"))
