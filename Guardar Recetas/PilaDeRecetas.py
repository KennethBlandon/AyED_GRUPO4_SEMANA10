# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

from gestor_recetas import Recetario

def main():
    recetario = Recetario()
    
    while True:
        print("\nMenú:")
        print("1. Agregar receta")
        print("2. Obtener próxima receta")
        print("3. Mostrar recetas en la cola")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            receta = input("Ingrese el nombre de la receta: ")
            recetario.agregar_receta(receta)
            print(f"Receta '{receta}' agregada.")

        elif opcion == "2":
            receta = recetario.obtener_proxima_receta()
            if receta:
                print(f"Receta entregada: {receta}")
            else:
                print("No hay recetas en la cola.")

        elif opcion == "3":
            recetas_pendientes = recetario.mostrar_recetas()
            print(f"Recetas en cola: {recetas_pendientes}")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
