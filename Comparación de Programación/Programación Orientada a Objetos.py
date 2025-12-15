# ============================================
# Programación Orientada a Objetos (POO)
# Cálculo del promedio semanal del clima
# ============================================

class ClimaSemanal:
    """
    Clase que representa el clima de una semana.
    """

    def __init__(self):
        # Encapsulamiento: atributo protegido
        self._temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal.
        """
        return sum(self._temperaturas) / len(self._temperaturas)


def main():
    """
    Función principal del programa.
    """
    print("=== Promedio Semanal del Clima (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()
