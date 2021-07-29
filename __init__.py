from flask import Flask
from Controller.login_controller import login
from View.versicherung_view import versicherung

app = Flask(__name__)




app.register_blueprint(login)
app.register_blueprint(versicherung)
