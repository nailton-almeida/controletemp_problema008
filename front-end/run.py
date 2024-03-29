# -*- encoding: utf-8 -*-
from flask_migrate import Migrate
from sys import exit
from decouple import *
from environment_state import *
from config import config_dict
from app import create_app, db

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True)
# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)


if __name__ == "__main__":
        app.run('0.0.0.0')

# @app.route('/')
# def index():
#     return render_template('index.html', temperatura=20)


#@app.route("/login")
# def home():
#     return render_template("index.html")
#app.run()
