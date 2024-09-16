from database import *
from flask import Flask, request, flash, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "BLÅHAJ@google.com"

@app.route("/", methods=['GET', 'POST'])
def home():
    query = request.form.get('query', '')
    quizzes = []
    try:
        sql = SQL()
        quizzes = sql.execute(f"SELECT ID, question, setter FROM quizzes WHERE question LIKE '%{query}%' AND visible = 1")
        flash(f"SQL Query Successful\nSELECT ID, question, setter FROM quizzes WHERE question LIKE '%{query}%' AND visible = 1", 'success')
    except sqlite3.OperationalError as e:
        print(e)
        flash(f"ERROR Processing SQL Query\nSELECT ID, question, setter FROM quizzes WHERE question LIKE '%{query}%' AND visible = 1", 'error')

    return render_template("index.html", quizzes = quizzes, query = query)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
