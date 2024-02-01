#Cohesión_y_acomplamiento.
#definimos_primero_la_cohesión.

def agregar_libro(biblioteca):
    titulo = input("Ingrese el titulo del libro:")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    disponiblidad = True
    libro = {"titulo": titulo, "autor": autor, "genero": genero, "disponibilidad":disponiblidad }
    biblioteca.append(libro)
    print(f'Libro"(titulo)" agregado a la biblioteca. ')

def prestar_libro(biblioteca):
    titulo = input("Ingrese el titulo del libro a pedir prestado: ")
    encontrado = False
    for libro in biblioteca:
        if libro["titulo"] == titulo and libro ["disponibilidad"]:
            libro["disponibilidad"] = False
            print(f'Libro"titulo" prestado con exito.')
            encontrado = True
            break
    if not encontrado:
        print(f'Libro "titulo" no disponible para préstamo.')

def devolver_libro (biblioteca):
    titulo = input("Ingrese el titulo del libro a devolver: ")
    encontrado = False
    for libro in biblioteca:
        if libro["titulo"] == titulo and not libro["disponiblidad"]:
            libro["disponibilidad"] = True
            print(f'Libro "{titulo}" devuelto exitosamente.')
            encontrado = True
            break 
    if not encontrado:
        print(f'No se puede devolver el libro "(titulo)".')

#acoplamiento 

def main():
    biblioteca = []

    while True:
         print("\n1. agregar libro")
         print("2. pedir prestado el libro")
         print("3. devolver libro")
         print("4. Salir")

         opcion = input("selecciona una opcion: ")

         if opcion == "1":
             agregar_libro(biblioteca)
         elif opcion == "2":
             prestar_libro(biblioteca)
         elif opcion == "3":
             devolver_libro(biblioteca)
         elif opcion == "4":
             print("Saliendo del programa ")
             break
         else:
             print("Opcion no valida. Seleccione la opcion correcta ")

if __name__ == "__main__":
    main()