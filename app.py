from flask import Flask, abort
import random

app = Flask(__name__)
Port = 80

def load_articles(filename="data.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

articles = load_articles()

@app.route("/")
def home_page():
    return "Hello from Home page"

@app.route('/article/<int:id>')
def article_by_id(id):
    if 0 <= id < len(articles):
        return articles[id]
    else:
        abort(404, description="Article not found")

@app.route('/article/random')
def random_article():
    rand = random.randint(0, len(articles) - 1)
    return articles[rand]

if __name__ == "__main__":
    app.run(debug=True, port=Port)
