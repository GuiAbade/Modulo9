# Desafio
from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
        'cancao': 'musica1',
        'estilo': 'hip-hop'
    },
    {
        'cancao': 'musica2',
        'estilo': 'rock'
    },
    {
        'cancao': 'musica3',
        'estilo': 'pop'
    }
]


# Define uma rota da aplicação que responde a requisições GET
@app.route('/cancoes', methods=['GET'])
def obter_todas_cancoes():  # que será executada quando a rota for acessada.
    # Retorna dados da variável cancoes em formato JSON como resposta da requisição.
    return jsonify(cancoes)


@app.route('/cancoes/<int:cancao_id>', methods=['GET'])
def obter_cancao_por_id(cancao_id):
    return jsonify(cancoes[cancao_id])


@app.route('/cancoes', methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(f'A canção {cancao} foi adicionada com sucesso', 200)


@app.route('/cancoes/<int:cancao_id>', methods=['PUT'])
def atualizar_cancao(cancao_id):
    cancao_alterada = request.get_json()
    cancoes[cancao_id].update(cancao_alterada)
    return jsonify(cancoes[cancao_id], 200)


@app.route('/cancoes/<int:cancao_id>', methods=['DELETE'])
def excluir_cancao(cancao_id):
    try:
        del cancoes[cancao_id]
        return jsonify({'mensagem': 'A canção foi excluída com sucesso!'})
    except:
        return jsonify('Não foi encontrada uma canção com esse id', 404)


app.run(port=500, host='localhost', debug=True)
