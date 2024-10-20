#imprime el nombre de la autora
print("JIMENE GAMBOA ISSIS ALEXA 3W")
print("no.1189")
#crear el diccionario a partir de las traducciones ingresadas
traducciones = input("Introduce las traducciones (formato: español:inglés, ...): ")
diccionario = {}

#procesar las traducciones manualmente
inicio = 0
for i in range(len(traducciones)):
    if traducciones[i] == ',' or i == len(traducciones) - 1:
        if i == len(traducciones) - 1:
            i += 1  # Incluir el último carácter
        par = traducciones[inicio:i].strip()
        esp_ing = par.split(':')
        diccionario[esp_ing[0].strip()] = esp_ing[1].strip()
        inicio = i + 1

# Pedir una frase en español y traducir
frase_espanol = input("Introduce una frase en español: ")
frase_traducida = ""

for palabra in frase_espanol.split():
    if palabra in diccionario:
        frase_traducida += diccionario[palabra] + " "
    else:
        frase_traducida += palabra + " "

# Mostrar la frase traducida
print("Frase traducida:", frase_traducida.strip())
