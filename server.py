from flask import Flask, request, jsonify
import json
import PipeANDStages

app = Flask(__name__)

@app.route('/pipeline', methods=['GET'])
def get_pipes():
    return jsonify({"Funis": PipeANDStages.get_funil()})

@app.route('/pipeline', methods=['POST'])
def post_pipes():
    payload = request.get_json()
    nome = payload.get('nome')
    response = PipeANDStages.criar_Funil(nome)
    return jsonify({"Resposta do Pipedrive": response})

if __name__ == "__main__":
    app.run()