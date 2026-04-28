""""
OBJETIVO GENERAL DEL PROYECTO: 
    GENERAR UNA FACTURA EN FORMATO PDF PARA UNA COMPAÑIA FICTICIA CON DATOS, VARIABLES Y CALCULACIONES DE IMPUESTOS AÑADIDOS.
"""
router_id = 1
cableLAN_id = 2
gatorade_id = 3
router_precio = 50
cableLan_precio = 5
gatorade_precio = 0.50

nombre = input("Nombre del cliente: ")
apellido = input("Apellido del cliente: ")
fecha = input(f"Fecha de la compra: ")
precio_item = input("Precio del item adquirido: ")
hora_instalacion = int(input("Horas de instalacion: "))
