from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Datos iniciales simulando dispositivos en la red
dispositivos = [
    {"id": 1, "name": "Switch1", "job": "Core"},
    {"id": 2, "name": "Firewall1", "job": "Seguridad"},
]

def encontrar_dispositivo(id):
    return next((d for d in dispositivos if d["id"] == id), None)

@app.route("/devices", methods=["GET"])
def get_devices():
    return jsonify(dispositivos)

@app.route("/devices/<int:id>", methods=["GET"])
def get_device(id):
    disp = encontrar_dispositivo(id)
    if disp:
        return jsonify(disp)
    else:
        abort(404, description="Dispositivo no encontrado")

@app.route("/devices", methods=["POST"])
def create_device():
    if not request.json or "name" not in request.json or "job" not in request.json:
        abort(400, description="Faltan campos requeridos")
    nuevo_id = max(d["id"] for d in dispositivos) + 1 if dispositivos else 1
    nuevo_disp = {
        "id": nuevo_id,
        "name": request.json["name"],
        "job": request.json["job"]
    }
    dispositivos.append(nuevo_disp)
    return jsonify(nuevo_disp), 201

@app.route("/devices/<int:id>", methods=["PUT"])
def update_device(id):
    disp = encontrar_dispositivo(id)
    if not disp:
        abort(404, description="Dispositivo no encontrado")
    if not request.json:
        abort(400, description="JSON inválido")
    disp["name"] = request.json.get("name", disp["name"])
    disp["job"] = request.json.get("job", disp["job"])
    return jsonify(disp)

@app.route("/devices/<int:id>", methods=["DELETE"])
def delete_device(id):
    disp = encontrar_dispositivo(id)
    if not disp:
        abort(404, description="Dispositivo no encontrado")
    dispositivos.remove(disp)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)

