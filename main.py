
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

articles = [
    {
        "id": 1,
        "title": "The Future of AI",
        "author": "Jane Doe",
        "date_published": "2023-01-01",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Suspendisse potenti. Sed cursus ante eget nibh sagittis, sit amet ultrices erat tincidunt."
    },
    {
        "id": 2,
        "title": "Climate Change: What You Need to Know",
        "author": "John Smith",
        "date_published": "2023-02-01",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Suspendisse potenti. Sed cursus ante eget nibh sagittis, sit amet ultrices erat tincidunt."
    },
    {
        "id": 3,
        "title": "The Rise of Virtual Reality",
        "author": "Mary Jones",
        "date_published": "2023-03-01",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget lacus eget nunc tincidunt laoreet. Suspendisse potenti. Sed cursus ante eget nibh sagittis, sit amet ultrices erat tincidunt."
    }
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = [article for article in articles if article["id"] == article_id][0]
    return render_template('article.html', article=article)

@app.route('/search')
def search():
    query = request.args.get('query')
    matching_articles = [article for article in articles if query in article["title"] or query in article["body"]]
    return render_template('index.html', articles=matching_articles)

if __name__ == '__main__':
    app.run(debug=True)
