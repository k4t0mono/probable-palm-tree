import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init the app
app = Flask(__name__)

# Config the data base
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', 'sqlite:///yiff.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Registering the routes
from routes import *
app.register_blueprint(app_person)
app.register_blueprint(app_yiff)
app.register_blueprint(app_main)


if __name__ == '__main__':
    port = os.getenv('PORT', 58913)

    app.run(host='0.0.0.0', port=port, debug=True)