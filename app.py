from flask import Flask, abort, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
Port = 80


def load_articles(filename="data.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

articles = load_articles()

@app.route('/article/<int:id>')
def article_by_id(id):
    if 0 <= id < len(articles):
        return jsonify({"quote": articles[id]})
    else:
        abort(404, description="Article not found")

@app.route('/article/random')
def random_article():
    rand = random.randint(0, len(articles) - 1)
    return jsonify({"quote": articles[rand]})

if __name__ == "__main__":
    app.run(debug=True, port=Port)