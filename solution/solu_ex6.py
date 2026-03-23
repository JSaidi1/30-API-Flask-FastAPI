"""
## Exercice 6: Blog Simple (CRUD Complet)

**Énoncé**:
Créez une API blog complète avec:
- `GET /posts` - Lister tous les articles
- `GET /posts/<id>` - Détail d'un article
- `POST /posts` - Créer un article
- `PUT /posts/<id>` - Modifier un article
- `DELETE /posts/<id>` - Supprimer un article

Structure d'un post:
```json
{
  "id": 1,
  "title": "Mon Premier Article",
  "content": "Contenu...",
  "author": "John",
  "created_at": "2024-01-01T10:00:00",
  "updated_at": "2024-01-01T10:00:00"
}
```
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

posts = []
next_id = 1


def find_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts), 200


@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = find_post(post_id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post), 200


@app.route("/posts", methods=["POST"])
def create_post():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    content = data.get("content")
    author = data.get("author")

    if not title or not content or not author:
        return jsonify({
            "error": "title, content and author are required"
        }), 400

    now = datetime.now().isoformat()

    post = {
        "id": next_id,
        "title": title,
        "content": content,
        "author": author,
        "created_at": now,
        "updated_at": now
    }

    posts.append(post)
    next_id += 1

    return jsonify(post), 201


@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    post = find_post(post_id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    content = data.get("content")
    author = data.get("author")

    if not title or not content or not author:
        return jsonify({
            "error": "title, content and author are required"
        }), 400

    post["title"] = title
    post["content"] = content
    post["author"] = author
    post["updated_at"] = datetime.now().isoformat()

    return jsonify(post), 200


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = find_post(post_id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    posts.remove(post)

    return jsonify({"message": "Post deleted successfully"}), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)