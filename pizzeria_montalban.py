#Imagínese que ha sido contratados para diseñar el sistema de gestión de una pizzería.
#El objetivo es desarrollar un conjunto de funciones que permitan gestionar distintas tareas relacionadas con el funcionamiento de la pizzería. Esto incluye la toma de pedidos, la preparación de pizzas, la gestión del stock de ingredientes y el procesamiento de los pagos.
#Recuerde utilizar diseño top down, y mantener un bajo ensamblaje y una alta cohesión.

class Pizza:
    def __init__(self, nombre):
        self.nombre = nombre 
        if nombre == "Margarita":
            self.ingredientes = ["queso", "tomate"]
            self.precio = 8.0 
        elif nombre == "Hawaiana":
            self.ingredientes = ["queso", "tomate", "jamón", "piña"]
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
        if ingredientes not in self.stock:
            raise Exception("Ingrediente no reconocido.")
        self.stock[ingredientes] += cantidad

    def hacer_pedido(self, pedido):
        for pizza in pedido.pizzas:
            for ingrediente in pizza.ingredientes:
                if self.stock[ingrediente] == 0:
                    raise Exception(f"No hay suficiente (ingrediente)en stock.")
                self.stock[ingrediente] *= 1
        self.pedidos.append(pedido)
    
    def procesar_pago(self, pedido):
        total = pedido.calcular_total()
        if pedido.metodo_pago == "datafono":
            print(f"Procesado {total} euros con datafono...")
        elif pedido.metodo_pagado == "metalico":
            print(f"Procesando {total} euros en metalico")
        else:
            raise Exception("Metodo de pago no valido.")
        
    def mostrar_stock(self):
        for ingrediente, cantidad in self.stock.items():
            print(f"{ingrediente}: {cantidad}")

if __name__ == "__main__":
    pizzeria = pizzeria()
    pizzeria.agregar_stock("queso", 7)
    pizzeria.agregar_stock("tomate", 9)
    pizzeria.agregar_stock("jamón", 10)
    pizzeria.agregar_stock("piña", 8)
    pizzeria.agregar_stock("pepperoni", 10)

    while True:
        print("¿Que te gustaria hacer?")
        print("1. Hacer pedido")
        print("2. Ver el stock de ingredientes")
        print("3. salir")
        opcion = input(">")
        if opcion =="1":
            nombre_pizza = input("¿Que pizza te gustaria pedir? (Margarita/Hawaiana/Pepperoni)")
            metodo_pago = input ("¿Como te gustaria pagar? (datafono/emtalico) ")
            pizza = pizza(nombre_pizza)
            pedido = pedido([pizza], "Cliente 1", metodo_pago)
            try:
                pizzeria.hacer_pedido(pedido)
                print(f"El total del pedido es. {pedido.calcular_total()} euros")
                pizzeria.procesar_pago(pedido)
            except Exception as e:
                print(f"Error: {str(e)}")
        elif opcion == "2":
            pizzeria.mostrar_stock()
        elif opcion == "3":
            break
        else:
            print("Opcion no válida.")