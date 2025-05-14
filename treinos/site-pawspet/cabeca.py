from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")
        print(f"Mensagem de {nome} ({email}): {mensagem}")
        return render_template("index.html", enviado=True)
    return render_template("index.html", enviado=False)

if __name__ == "__main__":
    app.run(debug=True)
