# ============================================
# Programación Tradicional
# Cálculo del promedio semanal del clima
# ============================================

def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas
    de los 7 días de la semana.
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main() -> None:
    """
    Función principal del programa.
    """
    print("=== Promedio Semanal del Clima (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()
