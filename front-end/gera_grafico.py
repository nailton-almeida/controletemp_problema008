import matplotlib
from pandas._libs.reshape import explode
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation

class Graficos():

    def gera_temp_grafico(self):

        plt.style.use('fivethirtyeight')

        x_vals = []
        y_vals = []

        index = count()


        data = pd.read_csv('temperatura_cofre_grafico.csv')
        # x = data['x_value']
        y1 = data['1']
        # y2 = data['total_2']
        plt.cla()

        plt.plot(y1, label='Temperatura')
        plt.legend(loc='upper left')
        plt.ylabel('Temperatura')
        plt.tight_layout()
        plt.savefig('app/base/static/graficos/temperatura.png')
        plt.cla()
        plt.clf()
        plt.close()
    def gera_temp_umidade(self):
        plt.style.use('fivethirtyeight')

        x_vals = []
        y_vals = []

        index = count()


        data = pd.read_csv('umidade_grafico.csv')
        # x = data['x_value']
        y1 = data['2']
        # y2 = data['total_2']
        plt.cla()

        plt.plot(y1, label='Umidade')

        plt.legend(loc='upper left')
        plt.ylabel('Umidade')
        plt.tight_layout()
        plt.savefig('app/base/static/graficos/umidade.png')
        plt.cla()
        plt.clf()
        plt.close()
    def gera_temp_externa(self):
        plt.style.use('fivethirtyeight')

        x_vals = []
        y_vals = []

        index = count()


        data = pd.read_csv('temp_externa.csv')
        # x = data['x_value']
        y1 = data['4']
        # y2 = data['total_2']
        plt.cla()

        plt.plot(y1 )

        plt.legend(loc='upper left')
        plt.ylabel('Temperatura Externa1')
        plt.tight_layout()
        plt.savefig('app/base/static/graficos/temp_externa.png')
        plt.cla()
        plt.clf()
        plt.close()
    def gera_ar_grafico(self):
        plt.style.use('fivethirtyeight')
        data = pd.read_csv('status_ar.csv')
        status = data['3']

        x=0
        y=0
        for i in status:

            if i == 'ON':
                x+=1
            else:
                y+=1
        sizes=[x,y]

        colors = ["#1f77b4", "#ff7f0e"]
        labels='ON','OFF'

        plt.pie(sizes, labels=labels, colors=colors)
        plt.title("Status ar condicionado")
        plt.savefig('app/base/static/graficos/arstatus.png')

# a = Graficos()
# a.gera_temp_externa()

