# Importar a classe Flask, objeto request e o objeto jsonify:
import math
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

pontos = [{'nome': 'x1', 'valor': 5},
{'nome': 'x2', 'valor': 2},
{'nome': 'y1', 'valor': 2},
{'nome': 'y2', 'valor': 3}]


# http://127.0.0.1:5000/pontos
@app.route('/pontos', methods=['GET'])
def retornar_todos_os_produtos_e_a_distancia():
    for distancia in pontos:
        distancia = int(pontos['nome'])
    return jsonify({'produtos': pontos, 'distancia':distancia})

# http://127.0.0.1:5000/pontos/x1
@app.route('/pontos/<string:nome>', methods=['GET'])
def retornar_dados_do_ponto_informado(nome):
    resp = {'ponto': '', 'valor': None}
    for ponto in pontos:
        if ponto['nome'] == nome:
            resp = ponto
    return jsonify(resp)

# http://127.0.0.1:5000/pontos/x1/3
@app.route('/pontos/<string:nome>/<int:valor>', methods=['POST'])
def inserir_produto(nome, valor):
    pontos.append({'ponto': nome, 'valor': valor})
    return jsonify({'ponto': nome, 'valor': valor})

# http://127.0.0.1:5000/pontos/x1/10
# http://127.0.0.1:5000/pontos/x1/-10
@app.route('/pontos/<string:nome>/<int(signed=True):valor>',
methods=['PATCH'])
def alterar_valor_do_ponto(nome, valor):
    resp = {'ponto': '', 'valor': None}
    for ponto in pontos:
        if ponto['nome'] == nome:
            ponto['valor'] += valor
            resp = ponto
    return jsonify(resp)

# http://127.0.0.1:5000/pontos/x1
@app.route('/pontos/<string:nome>', methods=['DELETE'])
def remover_ponto(nome):
    for i, ponto in enumerate(pontos):
        if ponto['nome'] == nome:
            del pontos[i]
    return jsonify({'pontos': pontos})



if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)