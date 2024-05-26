from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido a la página de recursos humanos"})

@app.route('/info')
def info():
    data = {
        "titulo": "EMPLEA GESTIÓN",
        "descripcion": (
            "Software de Recursos Humanos, EMPLEA GESTIÓN, ayuda a las empresas "
            "a gestionar eficientemente las tareas relacionadas con la gestión "
            "del personal y la administración de recursos humanos. Software personalizable "
            "según las necesidades específicas de cada empresa."
        ),
        "integrantes": [
            "Daniel Romero",
            "Nicolas Velazco",
            "Jose Luis Malagón",
            "Angie Gutierrez"
        ],
        "mensaje": "Ejemplo de Microservicio utilizando el contenedor Docker."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

