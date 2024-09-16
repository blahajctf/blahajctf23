from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/print', methods=["POST"])
def report():
    message = request.form['message']
    count = int(request.form['count'])
    return render_template_string(
        '<link rel="stylesheet" href="/static/style.css">\n'
        + f'<p>{message}</p>'*count
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
