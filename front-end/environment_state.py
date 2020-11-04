import random
import time
import json
import csv
from gerenciador import Subs

def dados_grafico_temp(temp_atual):

    fieldnames = ['1']
    with open('temperatura_cofre_grafico.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        temp = {
            '1': temp_atual,
        }
        csv_writer.writerow(temp)

def dados_grafico_umi(umidade):
    fieldnames = ["2"]
    with open('umidade_grafico.csv', 'a+') as csv_file:

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        umidade = {
            "2": umidade,
        }
        csv_writer.writerow(umidade)

def dados_status(status_ar):
    fieldnames = ["3"]
    with open('status_ar.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        status = {
            "3": status_ar,

        }
        csv_writer.writerow(status)

def dados_grafico_ext(temp_ext):
    fieldnames = ["4"]
    with open('temp_externa.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        status = {
            "4": temp_ext,

        }
        csv_writer.writerow(status)

def aumento_porta(min, max, temp, status_porta,):
    abertura = 0
    while status_porta == "Aberta":
      if status_porta == "Aberta":
        #abertura +=1
        temp += 0.00166*5
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

    umidade2 = round(random.uniform(60,90),2)
    temp_ex = round(random.uniform(30, 40), 2)

    pega_ambi = Subs()
    temperatura_interna, umidade,temp_externa = pega_ambi.subs_temp()
    temp_atual,status_ar = aumento_porta(min,max,temperatura_interna,status_porta)

    temp = {
        "temperature_cofre": temp_atual,
        "umidade": umidade2,
        "temp_externa": temp_ex,
    }
    tempfile = json.dumps(temp)
    with open('temp_interna.json', 'w+') as file:
        file.write(tempfile)

    dados_grafico_temp(temp_atual)
    dados_grafico_umi(umidade)
    dados_status(status_ar)
    dados_grafico_ext(temp_externa)

    #print(round(temp_atual,2),umidade,status_ar)
    return round(temp_atual,2),umidade,status_ar


# while True:
#     get_environment_status(23,24,'Aberta')
