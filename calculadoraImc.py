# calculadora de IMC
# formula = Peso / altura^2
# < 19 = delgadez
# Entre 20 y 25 = normal
# Entre 26 y 30 = sobrepeso
# > 30 = obesidad

peso = float(input("Ingrese su peso "))
altura = float(input("Ingrese su altura ")) / 100
imc = (peso/(altura*altura))
def calculadoraImc(peso, altura):
    if imc < 20:
        print("Usted se encuentra en delgadez")
    elif imc >= 20 and imc <= 25:
        print("Usted se encuentra normal")
    elif imc >= 26 and imc <= 30:
        print("Usted se encuentra en sobrepeso")
    else :
        print("Usted se encuentra en obesidad")

calculadoraImc(peso,altura)