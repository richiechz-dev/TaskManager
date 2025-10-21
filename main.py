def menu():  # Envolvemos el menu dentro de una funcion por buenas practicas
    print("Hello from taskmanager!")
    print("Menu Principal\n")
    print("1. Agregar una nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Salir()")


def main():
    menu()
    while True:  # Repite lo siguente para siempre
        try:
            opc = int(input("Selecciona una opcion: "))  # Ingresa una opción
            # Va a comparar en el siguiente orden si una opc coincide con la ingresada
            if opc == 1:
                pass
            elif opc == 2:
                pass
            elif opc == 3:
                pass
            elif (
                opc == 4
            ):  # Si coincide con la opcion 4 el programa finalizara con break y terminara el bucle
                print("Adiós usuario ...")
                break
            else:
                print(
                    "Opción no valida, intenta de nuevo..."
                )  # Cualquiera otro numero entero dira, el siguiente texto:
        except ValueError:
            print("Error inesperado, ingresaste una texto")


if __name__ == "__main__":
    main()
