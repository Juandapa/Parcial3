class Animal : 
    def _init_ (self, codigo, nombre, edad) : 
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.produccion = []



    def registrar_produccion(self, huevos) : 
        self.produccion.append



    def produccion_total(self) : 
        return sum(self.produccion)
    

    def _str_(self) : 
        return f"Codigo: {codigo}, Nombre: {nombre}, Edad: {edad}, Produccion total: {self.produccion_total()} huevos"
    


class BaseDatos : 
    def _init_(self) : 
        self.animales = []

    def crear_animal(self, animal) : 
        self.animales.append(animal)

    def leer_animal(self, codigo): 

        for a in self.animales : 
            if a.codigo == codigo : 
                return a
            
        return None 
    
    def actualizar_animal(self,codigo, nueva_raza = None, nueva_edad = None): 

        animal = self.leer_amnimal(codigo)

        if animal : 
            if nueva_raza
                animal.raza = nueva_raza
            if nueva_edad : 
                animal.edad = nueva_edad
            return True
        return False    
    
    def eliminar_animal(self, codigo) : 

        for a in self.animales : 
            if a.codigo == codigo : 
                self.animales.remove(a)
                return True
        return False
    

    class Interfaz : 
        def mostrar_menu(self) : 
            print("\n--- Sistema de Registro de Pollos ---")
            print("1. Agregar animal")
            print("2. Registrar producción semanal")
            print("3. Consultar producción")
            print("4. Actualizar datos del animal")
            print("5. Eliminar animal")
            print("6. Mostrar todos los animales")
            print("0. Salir")# main.py 
from modelo import Animal, BaseDatos, Interface

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