def celsius_fahrenheit(C: float) -> float:
    """Converte temperatura em Celsius para Fahrenheit.
    Fórmula: F = C * 9/5 + 32
    """
    return C * 9/5 + 32

def metros_quilometros(m: float) -> float:
    """Converte distância em metros para quilômetros.
    1 km = 1000m
    """
    return m / 1000

print(celsius_fahrenheit(12))
print(metros_quilometros(32))