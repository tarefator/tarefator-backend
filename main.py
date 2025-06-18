from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/resolver-tarefas', methods=['POST'])
def resolver_tarefas():
    data = request.json
    ra = data.get('ra')
    senha = data.get('senha')

    if not ra or not senha:
        return jsonify({'status': 'erro', 'mensagem': 'RA e senha são obrigatórios.'}), 400

    # Aqui será integrado o robô automatizado futuramente
    resultado = {
        'status': 'sucesso',
        'mensagem': f'Tarefas do RA {ra} resolvidas com sucesso (simulado).'
    }

    return jsonify(resultado)

app.run(debug=True, port=5000)
