# Tu código aquí

# Listar todos los usuarios

# Agregar un nuevo usuario. Para ello deberás solicitar el nombre y el número al usuario

# Modificar un usuario existente. Para ello deberás solicitar el nombre del cliente, buscarlo, y en caso de encontrarlo, solicitar el nuevo número. En caso de no encontrarlo, hazle saber al usuario que el nombre del cliente no existe.

# Eliminar un usuario existente.

# Salir


from data import people

while True:
    print("=====================================================================")
    print("Ingresa el numero 1 para ver los numeros de cada usuario")
    print("Ingresa el numero 2 para agregar un nuevo usuario a la lista")
    print("Ingrese el numero 3 para modificar un usuario existente")
    print("Ingrese el numero 4 para eliminar un usuario existente")
    print("Ingrese el numero 5 para salir")
    print("=====================================================================")
    print("")

    user_input = int(input())

    if user_input == 1:
        for key,value in people.items():
            print(f"{key}===> {value}")
    elif user_input == 2:
        nombre = input("Agrega el nombre del usuario: ")
        numero = (input(f"Agrega el numero del usuario: "))

        people[f"{nombre}"] = [f"{numero}"]
    elif user_input == 3:
        nombre_md = input("Ingrese el nombre del usuario: ")
        numero_md = (input(f"Ingrese el numero del usuario: "))

        people[f"{nombre_md}"] = [f"{numero_md}"]
    elif user_input == 4:
        nombre_del = input("Ingrese el nombre del usuario que desea eliminar: ")
            
        del people[f"{nombre_del}"]
    elif user_input == 5:
        break
    else:
        print("")
        print("Valor incorrecto, vuelve a intentar")
        print("")
