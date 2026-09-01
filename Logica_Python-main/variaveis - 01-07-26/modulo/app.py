from conversoes import celsius_fahrenheit, metros_quilometros

def main() -> None:
    # Exemplos de uso
    c = 25
    m = 1500
    print(f"{c}°c = {celsius_fahrenheit(c):.2f}°F")
    print(f"{m} m =  {metros_quilometros(m):.3f} km")

# Ponto de entrada do programa
# Só executa main() se este arquivo for o script principal
if __name__ == "__main__":
    main()