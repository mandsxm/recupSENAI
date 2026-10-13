from flask import Flask, render_template, redirect, request

app = Flask (__name__)

@app.route("/") 
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/inicio")
    return render_template("login.html")

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    return render_template("adicionar.html")

if __name__ == "__main__":
    app.run(debug=True)