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
            print("0. Salir")