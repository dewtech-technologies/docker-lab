from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Define o caminho do arquivo dentro de /tmp
    tmp_file_path = '/tmp/hello.txt'

    # Escreve uma mensagem no arquivo
    with open(tmp_file_path, 'a') as file:
        file.write('Hello from Flask Tmpfs!\n')

    # Retorna uma mensagem junto com o conteúdo do arquivo
    with open(tmp_file_path, 'r') as file:
        content = file.read()
    return "Hello from Flask Tmpfs! Here's the content of /tmp/hello.txt:\n" + content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

