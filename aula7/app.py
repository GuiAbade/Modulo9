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


app.run(port=5000, host='localhost', debug=True)
