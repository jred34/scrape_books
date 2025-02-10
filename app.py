from flask import Flask, render_template
from bookscraper import scrape_books
app = Flask(__name__)

@app.route("/")
def index():
    books = scrape_books()
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
