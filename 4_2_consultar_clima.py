from clima_utils import consultar_clima, imprimir_clima


# Consulta el clima de Popayán usando las funciones compartidas.
clima = consultar_clima(2.4419, -76.6063)
# Solo intenta mostrar los datos si la consulta tuvo éxito.
if clima is not None:
    imprimir_clima(clima)
