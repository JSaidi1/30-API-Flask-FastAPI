"""
## Exercice 1: Hello World Multilingue

**Énoncé**:
Créez une application Flask avec une route `/hello/<language>` qui retourne un message "Hello" dans la langue spécifiée.

Exemple d'usage:
```bash
curl http://localhost:5000/hello/english
# {"message": "Hello!", "language": "english"}

curl http://localhost:5000/hello/french
# {"message": "Bonjour!", "language": "french"}
```
"""
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello/<string:language>', methods=['GET'])
def hello(language):

    if language == "english":
        return jsonify({
            "message": f"Hello!",
            "language": "english",
            "status": "success"
        }), 200
    
    elif language == "french":
        return jsonify({
            "message": f"Bonjour!",
            "language": "french",
            "status": "success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": f"Language {language} do not exists",
        }), 400


  


  

if __name__ == '__main__':
    app.run(debug=True, port=5000)