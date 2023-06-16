def encriptar(texto):
    textoFinal = ""
    for letra in texto:
        textoFinal += letra + "x"
    return textoFinal

def desencriptar(texto):
    textoFinal = ""
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    textoArchivo = archivo.read()
    print("El texto a encriptar es: " + textoArchivo)
    archivo.close()
    archivo = open(rutaArchivo, "w")
    print("El texto encriptado es: " + encriptar(textoArchivo))
    archivo.write(encriptar(textoArchivo))
    archivo.close()

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    textoArchivo = archivo.read()
    print("El texto a desencriptar es: " + textoArchivo)
    archivo.close()
    archivo = open(rutaArchivo, "w")
    print("El texto desencriptado es: " + desencriptar(textoArchivo))
    archivo.write(desencriptar(textoArchivo))
    archivo.close()

def usoPrograma():
    rutaArchivo = input("Ingrese la ruta de su archivo de texto: ")
    print("Seleccione una opcion para archivo de texto:")
    print("A - Encriptar archivo")
    print("B - Desencriptar archivo")
    print("C - Salir")
    uso = input("> ")
    usoA = ["A","a"]
    usoB = ["B","b"]
    usoC = ["C","c"]
    if uso in usoA :
        encriptarArchivo(rutaArchivo)
    elif uso in usoB :
        desencriptarArchivo(rutaArchivo)
    elif uso in usoC :
        exit()
    else:
        print("Error al seleccionar la opcion, intente nuevamente.")
        usoPrograma()
        
usoPrograma()
