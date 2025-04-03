from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    print(f"Recibido: {data}")
    return jsonify({"message": "Estado actualizado"}), 200

@app.route('/get_commands', methods=['GET'])
def get_commands():
    return jsonify({"relay1": "ON", "relay2": "OFF"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
