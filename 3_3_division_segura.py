# Divide dos números y devuelve None si el divisor es cero.
def dividir_seguro(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        # Evita que el error detenga el programa y avisa qué ocurrió.
        print("No se puede dividir entre cero.")
        return None


# Prueba la función con una división válida y con divisor cero.
print("dividir_seguro(10, 2) =", dividir_seguro(10, 2))
print("dividir_seguro(5, 0) =", dividir_seguro(5, 0))
