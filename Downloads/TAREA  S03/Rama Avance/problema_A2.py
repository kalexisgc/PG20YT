"""
Cree una clase Persona en python con los atributos nombre y DNI, y cree un aplicativo con un menú con tres opciones:
1. Crear persona, donde pedirá los datos y creará una persona y la agregará a la lista.
2. Listar, donde mostrará todas las personas que hay en la lista.
3. Eliminar, donde pedirá un DNI y borrará a la persona que tenga ese DNI de la lista.
Habrá también una cuarta opción, que es Salir.
"""
class Persona: 
    def __init__(self, nombre, dni): 
        self.nombre = nombre 
        self.dni = dni 
    def __str__(self): 
        return f"{self.nombre} - {self.dni}"
    
personas = [] 
while True: 
    print("\n1.Crear 2.Listar 3.Eliminar 4.Salir") 
    op = input("Opción: ") 
    if op == "1": 
        nombre = input("Nombre: ") 
        dni = input("DNI: ") 
    if not any(p.dni == dni for p in personas): 
        personas.append(Persona(nombre, dni)) 
        print(" Creada") 
    elif op == "2": 
        for i, p in enumerate(personas, 1)
            print(f"{i}. {p}")
    elif op == "3": 
        dni = input("DNI a eliminar: ") 
        personas[:] = [p for p in personas if p.dni != dni] 
        print(" Eliminada" if any(p.dni == dni for p in personas) else " No encontrada") 
    elif op == "4": 
        break 
    else: 
        print(" Opción inválida")