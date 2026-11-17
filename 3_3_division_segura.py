def dividir_seguro(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
        return None


print("dividir_seguro(10, 2) =", dividir_seguro(10, 2))
print("dividir_seguro(5, 0) =", dividir_seguro(5, 0))
