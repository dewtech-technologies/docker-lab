from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, Mundo! Este é um exemplo básico do Flask rodando em Docker.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
