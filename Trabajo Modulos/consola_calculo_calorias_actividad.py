from src.calculadora_de_indices import calcular_calorias_en_actividad

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu genero [f/m]: ")
# "\n = sirve para tabular y poder escribir en una sola linea"
valor_actividad = input("Ingrese el numero segun corresponda a su actividad fisica: \n1: poco o ningún ejercicio\n2: ejercicio ligero (1 a 3 días a la semana)\n3: ejercicio moderado (3 a 5 días a la semana)\n4: deportista (6 -7 días a la semana)\n5: atleta (entrenamientos mañana y tarde)\n")

calculo_de_calorias = calcular_calorias_en_actividad (peso, altura, edad, genero,valor_actividad)

print (f"El valor de las calorias en actividad es {calculo_de_calorias}")
