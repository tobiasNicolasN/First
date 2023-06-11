#archivo = open("texto.txt", "a")
#archivo.write("Prueba de guardado")
#archivo.close()

def encriptar(texto):
    print("El texto a encriptar es: " + texto)
    textoFinal = ""
    for letra in texto:
        textoFinal += letra + "x"
    print("El texto encriptado es: " + textoFinal)

def desencriptar(texto):
    print("El texto a desencriptar es: " + texto)
    textoFinal = ""
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    print("El texto desencriptado es: " + textoFinal)

desencriptar("pxrxuxexbxax xdxex xexnxcxrxixpxtxaxdxox")

def encriptarArchivo():