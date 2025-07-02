from src.calculadora_de_indices import consumo_calorias_recomendado_para_adelgazar

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu genero [f/m]: ") # m = 10.8 / f = 0

# calorias_recomendadas_15 = ((tmb * 15) / 100)
# calorias_recomendadas_20 = ((tmb * 20) / 100)

respuesta_calorias_para_adelgazar = consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, genero)

print(respuesta_calorias_para_adelgazar)