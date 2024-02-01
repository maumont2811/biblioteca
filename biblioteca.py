#Cohesión_y_acomplamiento.

#definimos_primero.
def agregar_libro(biblioteca):
    titulo = input("Ingrese el titulo del libro:")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    disponiblidad = True
    libro = {"titulo": titulo, "autor": autor, "genero": genero, "disponibilidad":disponiblidad }
    