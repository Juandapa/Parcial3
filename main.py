from Modelo import Animal, BaseDatos, Interface

def main():
    bd = BaseDatos()
    ui = Interface()

    while True:
        ui.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del pollo: ")
            raza = input("Raza: ")
            edad = int(input("Edad (en semanas): "))
            animal = Animal(codigo, raza, edad)
            bd.crear_animal(animal)
            print("Animal agregado correctamente.")

        elif opcion == "2":
            codigo = input("Código del pollo: ")
            animal = bd.leer_animal(codigo)
            if animal:
                huevos = int(input("Cantidad de huevos producidos esta semana: "))
                animal.registrar_produccion(huevos)
                print("Producción registrada.")
            else:
                print("Animal no encontrado.")

        elif opcion == "3":
            codigo = input("Código del pollo: ")
            animal = bd.leer_animal(codigo)
            if animal:
                print(f"\n{animal}")
                print(f"Producción semanal: {animal.produccion}")
            else:
                print("Animal no encontrado.")

        elif opcion == "4":
            codigo = input("Código del pollo: ")
            nueva_raza = input("Nueva raza (dejar vacío si no cambia): ")
            nueva_edad = input("Nueva edad (dejar vacío si no cambia): ")
            nueva_edad = int(nueva_edad) if nueva_edad else None
            if bd.actualizar_animal(codigo, nueva_raza, nueva_edad):
                print("Datos actualizados.")
            else:
                print("Animal no encontrado.")

        elif opcion == "5":
            codigo = input("Código del pollo: ")
            if bd.eliminar_animal(codigo):
                print("Animal eliminado.")
            else:
                print("Animal no encontrado.")

        elif opcion == "6":
            print("\n--- Lista de animales ---")
            for a in bd.animales:
                print(a)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()  