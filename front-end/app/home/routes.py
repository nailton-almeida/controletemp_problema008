# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from environment_state import *
from app.home import blueprint
from flask import render_template, request, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
import json



@blueprint.route('/temperatura.html', methods=['GET', 'POST'])
@login_required
def controle_temperatura():
    if request.method == 'POST':

        if request.form["botao_porta"] == '2':
            status_porta = request.form["porta"]
            with open('temperaturas.json', 'r') as file:
                limites = file.read()
                limites = json.loads(limites)
                mini = limites["min"]
                max = limites["max"]

            porta = {
                'porta': status_porta
            }
            tempo_porta={

                'segundos': 0
            }
            d2_json = json.dumps(porta)
            d3_json = json.dumps(tempo_porta)
            with open('porta.json', 'w+') as file:
                file.write(d2_json)

            with open('tempo_porta.json','w+') as file:
                 file.write(d3_json)

            temp, umidade, status_ar = get_environment_status(mini, max, status_porta)
            return render_template('temperatura.html', temperatura=temp, umidade=umidade, status_ar=status_ar, min=mini,
                                   max=max, status_porta=status_porta)#, tempo_porta=abertura)

        # ELSE POST TEMPERATURA
        else:

            mini_post = float(request.form["minimo"])
            max_post = float(request.form["maximo"])

            limites = {
                'min': mini_post,
                'max': max_post,
            }
            d1_json = json.dumps(limites)
            with open('temperaturas.json', 'w+') as file:
                file.write(d1_json)

            with open('porta.json', 'r') as file:
                door = file.read()
                door = json.loads(door)
                status_porta = door["porta"]

            with open('tempo_porta.json', 'r') as file:
                tp = file.read()
                tp = json.loads(tp)
                tpa = tp["segundos"]

            tpa += 10

            tempo_porta = {

                'segundos': tpa
            }

            d4_json = json.dumps(tempo_porta)

            with open('tempo_porta.json', 'w+') as file:
                file.write(d4_json)

            temp, umidade, status_ar = get_environment_status(mini_post, max_post, status_porta)
            return render_template('temperatura.html', temperatura=temp, umidade=umidade, status_ar=status_ar,
                                   min=mini_post, max=max_post, status_porta=status_porta,tempo_porta=tpa)


    # ELSE PARA DIFERENCIAR GET
    else:

        with open('temperaturas.json', 'r') as file:
            limites = file.read()
            limites = json.loads(limites)
            mini = limites["min"]
            max = limites["max"]

        with open('porta.json', 'r') as file:
            door = file.read()
            door = json.loads(door)
            status_porta = door["porta"]

        temp, umidade, status_ar = get_environment_status(mini, max, status_porta)

        with open('tempo_porta.json', 'r') as file:
            tp = file.read()
            tp = json.loads(tp)
            tpa = tp["segundos"]

        tpa+=10
        tempo_porta = {

            'segundos': tpa
        }
        d4_json = json.dumps(tempo_porta)

        with open('tempo_porta.json', 'w+') as file:
            file.write(d4_json)

        return render_template('temperatura.html', temperatura=temp, umidade=umidade, status_ar=status_ar, min=mini,
                                   max=max, status_porta=status_porta, tempo_porta=tpa)



@blueprint.route('/index')
@login_required
def index():
    return render_template('page-blank.html')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(template, segment=segment)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
