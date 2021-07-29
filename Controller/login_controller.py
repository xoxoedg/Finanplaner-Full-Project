from flask import Blueprint, render_template, redirect, request


login = Blueprint("login", __name__, url_prefix="login")


@login.route("/")
def login_page():
    return render_template('LoginPage.html')

@login.route("/user", methods=["POST"])
def login_form(test):
    if request.method == "POST":

        return render_template('LoginForm.html')
    return

@login.route("/failed")
def login_form():
    pass


