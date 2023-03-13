from flask import Flask

app = Flask(__name__, static_url_path="", static_folder="web")



@app.route('/')
def index():
    return app.send_static_file("index.html")



app.run(host='0.0.0.0', port=81)
