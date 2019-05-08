import os
from flask import Flask, jsonify
from routes import app_yiff, app_main


app = Flask(__name__)
app.register_blueprint(app_yiff)
app.register_blueprint(app_main)


if __name__ == '__main__':
    port = os.getenv('PORT', 58913)
    app.run(host='0.0.0.0', port=port, debug=True)