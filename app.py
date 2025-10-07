import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    lista_de_usuarios = []
    try:
        with open('usuarios.json', 'r', encoding='utf-8') as arquivo:
            lista_de_usuarios = json.load(arquivo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    except json.JSONDecodeError:
        print("Erro: O arquivo contém erro de formatação ou está vazio.")

    return render_template('index.html', usuarios=lista_de_usuarios)


if __name__ == '__main__':
    app.run()
