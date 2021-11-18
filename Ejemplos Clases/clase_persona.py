# -*- coding: utf-8 -*-

# Se puede tener en otro archivo llamado persona.py y en una carpeta
# from persona import Persona

class Persona:
    # Se puede prescindir de esta parte si se desea. Si se prescinde, la propiedad se crea.
    # Útil para cuando se quiere tener propiedades predefinidas.
    nombre : str
    apellido_1 : str
    apellido_2 : str
    edad: float

    def __init__(self, nombre, apellido_1, apellido_2, edad):
        self.nom = nombre
        self.ap_1 = apellido_1
        self.ap_2 = apellido_2
        self.edad = edad
    
    def saludar(self):
        print("Hola, me llamo " + self.nom + " " + self.ap_1 + " " + self.ap_2 + " y tengo " + str(self.edad) + " años.")

# Se heredan métodos, propiedades y constructores: todo.
class Empleado(Persona):
    puesto: str
    precio_hora: float
    horas_trabajadas: int = 0
    
    # Definir constructor para definir empleados.
        # No se tienen que poner todas las propiedades: solo las que se quieran inicializar
    def __init__(self, nom, ap_1, ap_2, edad, puesto, precio_hora):
        super(Empleado, self).__init__(nom, ap_1, ap_2, edad)
        self.puesto = puesto
        self.pHora = precio_hora
        
    # Todos los métodos tienen self porque se van a usar parámetros de la clase.
    def trabajar(self, horas: int):
        self.horas_trabajadas += horas
        print(f"{self.nom} {self.ap_1} {self.ap_2} lleva {str(self.horas_trabajadas)} horas trabajadas.")
        
    def cobrar(self):
        print(f"{self.nom} {self.ap_1} {self.ap_2} ha cobrado {str(self.horas_trabajadas*self.pHora)}.")
        self.horas_trabajadas = 0


           
Lluna = Persona("Lluna", "Sanz", "Montrull", 24)   
Lluna = Empleado(Lluna.nom, Lluna.ap_1, Lluna.ap_2, Lluna.edad, "Data Engineer", 30)  
Lluna.saludar()
Lluna.trabajar(10)
Lluna.trabajar(10)
Lluna.trabajar(10)
Lluna.cobrar()
