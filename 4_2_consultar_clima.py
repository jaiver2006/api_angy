from clima_utils import consultar_clima, imprimir_clima


clima = consultar_clima(2.4419, -76.6063)
if clima is not None:
    imprimir_clima(clima)
