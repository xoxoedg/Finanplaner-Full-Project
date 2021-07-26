from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route("/")
def login_page():
    return render_template('LoginPage.html')

@app.route("/Login")
def login_form():
    return render_template('LoginForm.html')

@app.route("/view")
def login_view():
    return render_template('FirstView.html')

@app.route("/view/Versicherungen")
def versicherungen():
    return render_template('Versicherungen.html')



if __name__ == "__main__":
    app.run(debug=True)
    