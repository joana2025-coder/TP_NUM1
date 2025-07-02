def calcular_IMC(peso,altura): # Parametros son los que espera la funcion que le manden    
    # (indice de masa corporal) = (peso / altura elevada a2)
    imc = peso / (altura ** 2)

    if imc < 16:
        return round(imc,2),"Delgadez severa"
    elif 16 < imc < 16.99:
        return round(imc,2),"Delgadez moderada"
    elif 17 < imc < 18.49:
        return round(imc,2),"Delgadez aceptable"
    elif 18.5 < imc < 24.99:
        return round(imc,2),"Peso normal"
    elif 25 < imc < 29.99:
        return round(imc,2),"Sobrepeso"
    elif 30 < imc < 34.99:
        return round(imc,2),"Obesidad tipo I" 
    elif 35 < imc < 39.99:
        return round(imc,2),"Obesidad tipo II"
    elif 40 < imc < 49.99: 
        return round(imc,2),"Obesidad tipo III o mórbida"
    elif imc > 50: 
        return round(imc,2),"Obesidad tipo IV o extrema"
    else:
        return round(imc,2),"Valores no contemplados"

    # return round(imc,2)


def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    valor_del_imc,_ = calcular_IMC(peso, altura) 
    # %GC = 1.2 * IMC + 0.23 * edad(años) - 5.4 - valor_genero
    if valor_genero == "m":
        valor_genero_persona = 10.8
    elif valor_genero == "f":
        valor_genero_persona = 0
    else:
        return "Genero no reconocido"
  
    porc_grasa_corp = round((1.2 * valor_del_imc + 0.23 * edad - 5.4 - valor_genero_persona),2)
    
    if valor_genero == "m": 
        if 29 >= edad >= 20 and 20 >= porc_grasa_corp >= 11:
            print(f"Tu porcentaje de grasa como hombre {porc_grasa_corp} es el recomendado")
        elif 39 >= edad >= 30 and 21 >= porc_grasa_corp >= 12:
            print(f"Tu porcentaje de grasa como hombre {porc_grasa_corp} es el recomendado")
        elif 49 >= edad >= 40 and 23 >= porc_grasa_corp >= 14:
            print(f"Tu porcentaje de grasa como hombre {porc_grasa_corp} es el recomendado")
        elif 59 >= edad >= 50 and 24 >= porc_grasa_corp >= 15:
            print(f"Tu porcentaje de grasa como hombre {porc_grasa_corp} es el recomendado")
        else:
            print(f"Tu porcentaje de grasa como hombre no es recomendado {porc_grasa_corp}")
    elif valor_genero == "f":
        if 29 >= edad >= 20 and 28 >= porc_grasa_corp >= 16:
            print(f"Tu porcentaje de grasa como mujer {porc_grasa_corp} es el recomendado")
        elif 39 >= edad >= 30 and 29 >= porc_grasa_corp >= 17:
            print(f"Tu porcentaje de grasa como mujer {porc_grasa_corp} es el recomendado")
        elif 49 >= edad >= 40 and 30 >= porc_grasa_corp >= 18:
            print(f"Tu porcentaje de grasa como mujer {porc_grasa_corp} es el recomendado")
        elif 59 >= edad >= 50 and 31 >= porc_grasa_corp >= 19:
            print(f"Tu porcentaje de grasa como mujer {porc_grasa_corp} es el recomendado")
        else:
            print(f"Tu porcentaje de grasa como mujer no es recomendado {porc_grasa_corp}")   
    return porc_grasa_corp

# TMB
def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    try:
        # m = 5
        # f = -161
        altura_en_cm = altura * 100 # 175 * 100
        if valor_genero == "m":
            valor_genero_persona = 5
        elif valor_genero == "f":
            valor_genero_persona = -161
        else: # DEFAULT
            return "Genero no reconocido"
        
        tmb = (10 * peso) + (6.25 * altura_en_cm) - (5 * edad) + valor_genero_persona
        
        return round(tmb,2)
    except ValueError as error:
        return error
 

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
 
    try: 
        if valor_actividad == "1":
            actividad_fisica = 1.2
        elif valor_actividad == "2":
            actividad_fisica = 1.375
        elif valor_actividad == "3":
            actividad_fisica = 1.55
        elif valor_actividad == "4":
            actividad_fisica = 1.72
        elif valor_actividad == "5":
            actividad_fisica = 1.9
        else:
            return "Ingrese valor de 1 a 5"

        valor_tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
        tmb_act_fisica = valor_tmb * actividad_fisica

        return round(tmb_act_fisica,2)
    except ValueError as error:
            return error


def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_maximas_recomendadas = round(tmb - ((tmb * 15) / 100),2)
    calorias_minimas_recomendadas = round(tmb - ((tmb * 20) / 100),2)
    return f"Para adelgazar es recomendado que consumas entre: {calorias_minimas_recomendadas} y {calorias_maximas_recomendadas} calorías al día."
    
     


# (porcentaje de grasa corporal) establece si una persona

# # (tasa metabolica) calcula la cantidad de calorías que una persona quema estando en reposo
# tmb = ((10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero)

# # (tasa metabolica s/act. fisica) calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física
# tmb_act_fisica = (tmb * valor_actividad)

# # (calculo de cal. diarias) calcula el rango de calorías recomendado para adelgazar
# calorias_recomendadas = ((tmb * 15) / 100)
    