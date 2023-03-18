from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="web")
PROJECTS = [
  {
    'id' : 1,
    'name': 'Eurorun',
    'type': 'unity video game project',
    'priorty':' Medium'
  },

  {
    'id' : 2,
    'name': 'school-shooter',
    'type': 'unity video game project',
    'priorty':'Low'
  },

  {
    'id' : 3,
    'name': 'Traze Auto Edit',
    'type': 'Editor made using python',
    'priorty':'Low'
  }
]


@app.route('/')
def index():
    return render_template("index.html", jobs=PROJECTS, company_name='Jovian')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

