#imprime los datos de la autora
print("JIMENE GAMBOA ISSIS ALEXA 3W")
print("no.1189")

#crear un diccionario vacío
persona = {}

#pedir información al usuario
while True:
    clave = input("Introduce una clave (nombre, edad, sexo, teléfono, correo electrónico) o 'salir' para terminar: ")
    if clave.lower() == 'salir':
        break
    valor = input(f"Introduce el valor {clave} para:")
    persona[clave] = valor
    print("Contenido del diccionario:", persona)
