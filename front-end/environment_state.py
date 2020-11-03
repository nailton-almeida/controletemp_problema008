from gerenciador import *
import random
import time
#global status_ar

def aumento_porta(min, max, temp, status_porta,):
    abertura = 0
    while status_porta == "Aberta":
      if status_porta == "Aberta":
        #abertura +=1
        temp += 0.00166*10
        status_arcondicionado = ar_condicionado(min,max,temp)
      return status_arcondicionado

    else:
        status_arcondicionado = ar_condicionado(min,max,temp)
        return status_arcondicionado

def ar_condicionado(min,max,temp):
    temp_ar = temp

    if temp < min:
        temp_ar += 0.01*10
        status_ar ="ON"
        return temp_ar,status_ar
    elif temp > max:
        temp_ar -= 0.01*10
        status_ar = "ON"
        return temp_ar, status_ar
    else:
        status_ar = "OFF"
        return temp_ar,status_ar



def get_environment_status(min,max,status_porta):

    pega_ambi = Subs()
    temperatura_interna, umidade = pega_ambi.subs_temp()
    temp_atual,status_ar = aumento_porta(min,max,temperatura_interna,status_porta)

    temp = {
        "temperature_cofre": temp_atual,
        "umidade": umidade,
        "temperature_antisala": 25,
    }
    tempfile = json.dumps(temp)
    with open('temp_interna.json', 'w+') as file:
        file.write(tempfile)

    #print(round(temp_atual,2),umidade,status_ar)
    return round(temp_atual,2),umidade,status_ar

