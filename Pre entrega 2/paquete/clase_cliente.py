class Cliente:
    def __init__(self, nombre, edad, mail, direccion):
        self.nombre = nombre
        self.edad = edad
        self.mail = mail
        self.direccion = direccion
    
    def comprar(self, articulo, precio):
        print(f"El cliente {self.nombre} compró '{articulo}' a un precio de u$d{precio}")

    def correo_promocional(self):
        print(f"Se ha enviado un correo promocional a {self.mail}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.mail}, Dirección: {self.direccion}"



