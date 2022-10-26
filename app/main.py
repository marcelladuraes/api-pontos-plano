from flask import Flask, request, jsonify
import math
app = Flask(__name__)

# http://127.0.0.1:5000/pontos
@app.route('/pontos/<float:x1>/<float:y1>/<float:x2>/<float:y2>', methods=['POST'])
def inserir_pontos(x1, y1, x2, y2):
    
    distancia = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))

    return jsonify({'Distância entre os pontos': distancia})

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)