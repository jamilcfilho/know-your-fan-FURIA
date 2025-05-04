from flask import Flask, render_template, request, redirect, url_for, flash
from helpers import validar_documento, validar_link
import os

app = Flask(__name__)
app.secret_key = "chave_secreta"

# Armazena os dados temporariamente
dados_cadastrados = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        endereco = request.form.get("endereco")
        cpf = request.form.get("cpf")
        interesses = request.form.get("interesses")
        email = request.form.get("email")
        eventos = request.form.get("eventos")
        compras = request.form.get("compras")
        links = request.form.get("links")
        doc = request.files["documento"]

        if doc and validar_documento(doc.filename):
            caminho = os.path.join("static", doc.filename)
            doc.save(caminho)

            if not validar_link(links):
                flash("Link inválido! Deve começar com http:// ou https://", "erro")
                return redirect(url_for("index"))

            dados_cadastrados.append({
                "nome": nome,
                "endereco": endereco,
                "cpf": cpf,
                "interesses": interesses,
                "email": email,
                "eventos": eventos,
                "compras": compras,
                "links": links,
                "documento": doc.filename
            })

            return redirect(url_for("sucesso"))

        flash("Documento inválido. Envie apenas arquivos PDF.", "erro")
        return redirect(url_for("index"))

    return render_template("index.html")


@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html", dados=dados_cadastrados)


if __name__ == "__main__":
    app.run(debug=True)
