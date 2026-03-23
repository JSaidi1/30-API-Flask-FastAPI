"""
## Exercice 2: Convertisseur de Température

**Énoncé**:
Créez une route `/convert/temp` qui accepte deux paramètres query:
- `value`: la température (nombre)
- `unit`: "c2f" (Celsius to Fahrenheit) ou "f2c" (Fahrenheit to Celsius)

Exemple:
```bash
curl "http://localhost:5000/convert/temp?value=25&unit=c2f"
# {"celsius": 25, "fahrenheit": 77.0}

curl "http://localhost:5000/convert/temp?value=77&unit=f2c"
# {"fahrenheit": 77, "celsius": 25.0}
```
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/convert/temp', methods=['GET'])
def convert_temp():

    value = request.args.get('value')
    unit = request.args.get('unit')

    if value and unit:

        value = float(value)

        # Celsius → Fahrenheit (F=(9/5)*​C + 32)
        if unit == "c2f":
            F = (9/5) * value + 32

            return jsonify({
                "celsius": value,
                "fahrenheit": F,
                "status": "success"
            }), 200

        # Fahrenheit → Celsius (C=(5/9)*​(F - 32))
        elif unit == "f2c":
            C = (5/9) * (value - 32)

            return jsonify({
                "fahrenheit": value,
                "celsius": C,
                "status": "success"
            }), 200
        
        # Other (error)
        else:
            return jsonify({
            "success": False,
            "error": "Bad request"
             }), 400

    else:
        return jsonify({
            "success": False,
            "error": "value query and unit query are required"
        }), 400

    

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

