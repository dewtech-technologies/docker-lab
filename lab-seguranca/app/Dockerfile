FROM python:3.8-slim

# Cria um usuário não root
RUN useradd -m myuser
USER myuser

# Define o diretório de trabalho
WORKDIR /home/myuser/app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Define o comando para executar a aplicação
CMD ["python", "app.py"]
