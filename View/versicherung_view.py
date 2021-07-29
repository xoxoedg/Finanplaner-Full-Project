from flask import Blueprint, render_template

versicherung = Blueprint("versicherung", __name__ ,url_prefix="/versicherung")


@versicherung.route("/view")
def login_view():
    return render_template('FirstView.html')

@versicherung.route("/view/Versicherungen")
def versicherungen():
    return render_template('Versicherungen.html')
