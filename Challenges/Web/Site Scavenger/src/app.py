from flask import Flask, render_template, request, render_template_string, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(): return render_template('/index.html')

@app.route('/about', methods=['GET'])
def about(): return render_template('/about.html')

@app.route('/sup3r-s3cr3t', methods=["GET", "POST"])
def hidden():
    if request.method == "GET":
        return render_template_string(
            "<p>GET functionality still in development</p><br>" +
            "<!-- TODO: Make this page request automatically POST -->"
        )
    
    if "fav_plush" not in request.form: return "What is your fav_plush?"
    
    if request.form['fav_plush'].lower() != "blahaj": return "Imposter, you are not the creator of this challenge"

    return render_template_string(
            """
            Welcome back, here is the 3rd part of the flag.<br>
            <code>1d_70o_^_^}</code>
            <br>Did you remember to collect the other 2 on the way?"""
        )

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
