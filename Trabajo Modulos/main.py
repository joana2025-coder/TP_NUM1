from src.calculadora_de_indices import calcular_IMC, calcular_porcentaje_grasa, calcular_calorias_en_reposo, calcular_calorias_en_actividad, consumo_calorias_recomendado_para_adelgazar

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu genero [f/m]: ") # m = 10.8 / f = 0
valor_actividad = input("Ingrese el numero segun corresponda a su actividad fisica: \n1: poco o ningún ejercicio\n2: ejercicio ligero (1 a 3 días a la semana)\n3: ejercicio moderado (3 a 5 días a la semana)\n4: deportista (6 -7 días a la semana)\n5: atleta (entrenamientos mañana y tarde)\n")

respuesta_de_imc, mensaje = calcular_IMC(peso,altura)
respuesta_porcentaje_grasa = calcular_porcentaje_grasa(peso, altura, edad, genero)
respuesta_calorias_reposo = calcular_calorias_en_reposo(peso, altura, edad, genero)
respuesta_calorias_actividad = calcular_calorias_en_actividad(peso, altura, edad, genero, valor_actividad)
respuesta_recomendacion_adelgazar = consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)

print (f"El valor del imc es: {respuesta_de_imc} y tu caracteristica es: {mensaje}")
print (f" El valor de tmb es: {respuesta_porcentaje_grasa}")
print (f" El valor de tmb en reposo es: {respuesta_calorias_reposo}")
print (f"El valor de las calorias en actividad es {respuesta_calorias_actividad}")
print(respuesta_recomendacion_adelgazar)