# Usa uma imagem base oficial do Python como ponto de partida
FROM python:3.8-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos 'requirements.txt' para o diretório atual de trabalho (/app) no container
COPY requirements.txt .

# Executa o comando para instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do seu projeto para o diretório de trabalho no container
COPY .. .

# Define o comando para rodar a aplicação
CMD ["python", "app.py"]
