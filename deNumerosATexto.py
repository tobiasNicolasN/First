numerosATexto = {
    "0": "Cero",
    "1": "Uno",
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve"
}
texto = input("Escriba un numero: ")
numeros = list(texto)
final = ""
for numero in numeros :
    final += numerosATexto[numero] + " "
print(final) 