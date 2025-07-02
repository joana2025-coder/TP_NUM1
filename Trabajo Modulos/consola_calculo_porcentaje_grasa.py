from src.calculadora_de_indices import calcular_porcentaje_grasa

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu genero [f/m]: ") # m = 10.8 / f = 0

porcentaje_grasa = calcular_porcentaje_grasa (peso, altura, edad, genero)
# "Genero no reconocido"
# string = Cadena de texto
# integer = Numero entero
# booleano = True o False
# float = Numero decimal

if type(porcentaje_grasa) is not str:
    print (f"El valor del porcentaje de grasa es {round(porcentaje_grasa,2)}")
    print(type(porcentaje_grasa))
else:
    # porcentaje_grasa = string
    print (f"El valor del porcentaje de grasa es {porcentaje_grasa}")
    print(type(porcentaje_grasa))