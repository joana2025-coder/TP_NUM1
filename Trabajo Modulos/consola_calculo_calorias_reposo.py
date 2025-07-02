from src.calculadora_de_indices import calcular_calorias_en_reposo

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu genero [f/m]: ")

calorias_en_reposo = calcular_calorias_en_reposo (peso, altura, edad, genero)

print (f" El valor de tmb en reposo es: {calorias_en_reposo}")