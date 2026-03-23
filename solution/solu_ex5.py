"""
## Exercice 5: Calculatrice API

**Énoncé**:
Créez une route `/calculate` qui accepte:
- `operation`: "add", "subtract", "multiply", "divide"
- `a`: premier nombre
- `b`: deuxième nombre

Exemple:
```bash
curl "http://localhost:5000/calculate?operation=add&a=10&b=5"
# {"operation": "add", "a": 10, "b": 5, "result": 15}

curl "http://localhost:5000/calculate?operation=divide&a=10&b=0"
# {"error": "Cannot divide by zero"}
```
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    a = request.args.get('a')
    b = request.args.get('b')

    # Validation des paramètres
    if not operation or not a or not b:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400

    # Logique des opérations
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 400

    # Réponse
    return jsonify({
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

