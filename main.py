from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario para almacenar el estado de los relés
relay_status = {
    "relay1": "OFF",
    "relay2": "OFF"
}

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    if "relay1" in data:
        relay_status["relay1"] = data["relay1"]  # Actualiza el estado del relé 1
    if "relay2" in data:
        relay_status["relay2"] = data["relay2"]  # Actualiza el estado del relé 2
    print(f"Nuevo estado: {relay_status}")
    return jsonify({"message": "Estado actualizado"}), 200

@app.route('/get_commands', methods=['GET'])
def get_commands():
    return jsonify(relay_status), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
