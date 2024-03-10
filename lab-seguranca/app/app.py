from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Configuração do Banco de Dados
DB_NAME = "postgres"
DB_USER = "postgres"
DB_HOST = "db"  # Nome do serviço no Docker Compose
DB_PORT = "5432"

@app.route('/test_db')
def test_db():
    try:
        # Ler a senha do arquivo de segredo
        with open('/run/secrets/db_password', 'r') as file:
            DB_PASS = file.read().strip()

        # Conectar ao banco de dados
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        
        # Testar a conexão
        return "Conexão com o banco de dados bem-sucedida!"
        
    except Exception as e:
        return f"Erro ao conectar com o banco de dados: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)