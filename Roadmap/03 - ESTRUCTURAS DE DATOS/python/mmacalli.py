#lista
from reflex.components.el import option
from reflex.style import breakpoints

my_list = ["brais", "black", "wolfy", "vision"]
print(my_list)
my_list.append("castor")#insercion
my_list.append("castor")
print(my_list)
my_list.remove("brais")#eliminar
print(my_list)
print(my_list[1])#acceder a posicion
my_list[1]= "loquito"#actualizar o cambiar nombre
print(my_list)
my_list.sort()#ordena
print(my_list)

#tuplas
my_tuple: tuple = ("martin", "maca", "@bruma", "49")
print(my_tuple[1])
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(type(my_tuple))

#sets
my_set = {"martin", "maca", "@bruma", "49"}
print(my_set)
my_set.add("vinoteca")
my_set.add("vinoteca")#no imprime la segunda version
print(my_set)
my_set.remove("martin")
print(my_set)
my_set = set(sorted(my_set))
print(type(my_set))

#Diccionario
my_dict: dict= {
    "nombre": "martin",
    "surname":"maca",
    "correo electronico":"@bruma",
    "age":"49"
} #clave valor no se pueden ordenar solo en el Phyton se puede
my_dict["alias"] = "negro" #insercion
print(my_dict["surname"]) # se accede por la clave
my_dict["age"] = "50" #actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items()))#ordenacion
print(type(my_dict))
"""
Extra
"""
def my_agenda():

    agenda = {}

    while True:

        print("")
        print("1.Buscar contacto")
        print("2.insertar contacto")
        print("3.Actualizar contacto")
        print("4.eliminar contacto")
        print("5.salir")

        option = input("\n selecciona una opcion")

        match option:
            case "1":
                name = input("introduce el nombre del contacto a buscar:   ")
                if name in agenda:
                    print(f"el numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"el contacto {name} no existe.")
            case "2":
                name = input("introduce el nombre del contacto")
                phone = input("introduce el numero telefonico del contacto")
                if phone.isdigit() and len(phone)> 0 and len(phone) <= 11:
                    agenda[name]=phone
            case "3":
                name = input("introduce el nombre del contacto a Actualizar:   ")
                if name in agenda:
                    phone = input("introduce el numero telefonico del contacto")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("debes introducir un telefono de 11 maximo")
                else:
                    print(f"el contacto {name} no existe.")
            case "4":
                name = input("introduce el nombre del contacto a eliminar:   ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"el contacto {name} no existe.")
            case "5":
                print("saliendo de la agenda")
                break
            case _:
                print("opcion no valida. elige una de 1 a 5")

my_agenda()