
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
    


