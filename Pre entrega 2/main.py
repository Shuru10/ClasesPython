from paquete.clase_cliente import Cliente


cliente1 = Cliente("Jorge", "36", "jorgito@gmail.com", "Calle Siempre Viva 123")
print(cliente1)

cliente1.comprar("Hollow Knight para PS4", 12.99)

cliente1.correo_promocional()
