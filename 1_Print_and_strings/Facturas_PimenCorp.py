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

print("Gracias por comprar en PimenCorp!, a continuacion desarrollaremos su factura.")
nombre = input("Nombre del cliente: ")
apellido = input("Apellido del cliente: ")
fecha = input("Fecha de la compra: ")
item = input("Item adquirido: ")
precio_item = float(input("Precio del item adquirido: "))
unidades = int(input("Cuantas unidades? "))
subtotal = precio_item * unidades
impuestos = subtotal * 0.15
print("")
print("")
print(f"Hola {nombre} {apellido}!, haz comprado {unidades} unidades de {item} el dia {fecha}.")
print("")
print(f"Subtotal: ${subtotal}, impuestos añadidos (IVA 15%): ${impuestos:.2f}")
print("")
print(f"Total de su compra: ${impuestos + subtotal:.2f}")
print("")
print("")
print("")
print("Su recibo, estimado comprador:")
print("")
print("")
print(f"""========================================
           FACTURA DE VENTA             
========================================
CLIENTE: {nombre} {apellido}
FECHA:   {fecha}
----------------------------------------
ITEM:    {item}
CANT:    {unidades}
PRECIO:  ${precio_item}
----------------------------------------
SUBTOTAL:          ${subtotal}
IVA (15%):         ${impuestos:.2f}
TOTAL A PAGAR:     ${subtotal + impuestos:.2f}
========================================""")
print("")
print("Muchas gracias por comprar con nosotros!, Vuelva pronto!")