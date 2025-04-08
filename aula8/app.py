# NOSSO 1° API - FLASK e DJANGO
# FLASK e FLASK RESTFUL

from flask import Flask, jsonify, request
postagens = [
    {
        'titulo': 'Minha Historia',
        'autor': 'Amanda Dias'
    },
    {
        'titulo': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'titulo': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]
app = Flask(__name__)

# Rota padrão - GET http://localhost:5000/


@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Criar uma nova postagem - POST - GET http://localhost:5000/postagem


@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagem.append(postagem)

    return jsonify(postagem, 200)

# Alterar postage, existente - PUT


@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    return jsonify(postagens[indice], 200)


app.run(port=5000, host='localhost', debug=True)
