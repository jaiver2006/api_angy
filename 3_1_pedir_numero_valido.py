while True:
    try:
        numero = float(input("Escribe un número: "))
        break
    except ValueError:
        print("Eso no es un número válido. Inténtalo de nuevo.")

print("Número recibido:", numero)
