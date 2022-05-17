from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from datetime import timedelta

app = Flask(__name__)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False # Token nunca expira
#app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=3)# Token expira en 3 minutos
app.config["JWT_SECRET_KEY"] = "Ge0HomeIsThePlaceWhereFantasyMeetsReality" 
jwt = JWTManager(app)

users = {} # Lista de usuarios - JWT

@app.route("/")
def hello_world():
    return {"text": "Hello and welcome to the CTF challenge!"}


if __name__ == "__main__":
    app.run(host="0.0.0.0") # Visible on the network not localhost only
