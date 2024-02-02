#Imagínese que ha sido contratados para diseñar el sistema de gestión de una pizzería.
#El objetivo es desarrollar un conjunto de funciones que permitan gestionar distintas tareas relacionadas con el funcionamiento de la pizzería. Esto incluye la toma de pedidos, la preparación de pizzas, la gestión del stock de ingredientes y el procesamiento de los pagos.
#Recuerde utilizar diseño top down, y mantener un bajo ensamblaje y una alta cohesión.

class Pizza:
    def __init__(self, nombre):
        self.nombre = nombre 
        if nombre == "Margarita":
            self.ingredientes = ["queso", "tomate"]
            self.precio = 8.0 
        elif nombre == "hawaina":
            self.ingredientes = ["queso", "tomate", "jamon", "piña"]
            self.precio = 9.5
        elif nombre == "Pepperoni":
            self.ingredientes = ["queso", "tomate", "pepperoni"]
            self.precio = 10.0
        else:
            raise Exception("tipo de pizza no reconocido. ")
        
class pedido:
    def __init__(self, pizzas, cliente, metodo_pago):
        if not isinstance(pizzas, list) or len(pizzas) == 0:
            raise Exception("Metodo de pago no válido. ")
        self.pizzas = pizzas
        self.cliente = cliente
        self.metodo_pago = metodo_pago
    
    def calcular_total(self):
        return sum(pizza.precio  for pizza in self.pizzas)

class pizzeria:
    def __init__(self):
        self.stock = {"queso":0, "tomate":0, "jamon":0, "piña":0, "pepperoni":0}
        self.pedido = []
    
    def agregar_stock(self, ingredientes, cantidad):
        