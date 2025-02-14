from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hello World</h1>"

@app.route('/<plataforma>/resumo')
def platform_summary(plataforma):
  return "<h1>Resumo: {}</h1>".format(plataforma)

@app.route('/<plataforma>')
def platform(plataforma):
  return "<h1>plataforma {}</h1>".format(plataforma)

@app.route("/geral/resumo")
def general_summary():
  return "<h1>Resumo Geral</h1>"

@app.route('/geral')
def general():
  return "<h1>Geral</h1>"

if __name__ == "__main__":
  app.run(debug=True)