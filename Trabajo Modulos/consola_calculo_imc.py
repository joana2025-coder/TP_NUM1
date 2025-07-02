from src.calculadora_de_indices import calcular_IMC

# # pedir al usuario que ingrese su peso y su altura
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
# # edad = int(input("Ingresa tu edad: "))
# # genero = input("Ingresa tu genero [f/m]: ")
# # valor_genero = 0
# # valor_actividad = 0

imc, mensaje = calcular_IMC(peso,altura) #26.45 / 20.31
print (f"El valor del imc es: {imc} y tu caracteristica es: {mensaje}")

# round() / 1er parametro el valor que queres redondear, 2do cuantos digitos queres que tenga



