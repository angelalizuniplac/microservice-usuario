# Define a imagem base do container e a versão slim é mais leve, contendo apenas pacotes essenciais
FROM python:3-slim-buster

# Define o diretório de trabalho dentro do container
# Todos os comandos subsequentes serão executados neste diretório
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt ./

# Instala as dependências Python listadas no requirements.txt
# --no-cache-dir: não mantém cache dos pacotes, reduzindo tamanho da imagem
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório local para o diretório de trabalho do container
# Isso inclui o código da aplicação e arquivos de configuração
COPY . .

# Define o comando padrão executado quando o container iniciar
# Executa o framework Nameko (microserviços Python) com:
# - run: comando para executar um serviço
# - --config config.yaml: arquivo de configuração do serviço
# - ServiceFuncoes: nome do módulo/serviço a ser executado
CMD ["nameko", "run", "--config", "config.yaml", "ServiceFuncoes"]

# ServiceFuncoes alternar entre usuario e funcoes