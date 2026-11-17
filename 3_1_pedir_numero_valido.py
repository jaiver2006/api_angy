# Repite la pregunta hasta que la entrada se pueda convertir a número.
while True:
    try:
        numero = float(input("Escribe un número: "))
        # Sale del ciclo cuando se recibe un valor numérico válido.
        break
    except ValueError:
        # Informa del error y permite que la persona vuelva a intentarlo.
        print("Eso no es un número válido. Inténtalo de nuevo.")

# Muestra el número que se convirtió correctamente.
print("Número recibido:", numero)
