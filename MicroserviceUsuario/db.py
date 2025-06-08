# SQLAlchemy é uma biblioteca Python que fornece um ORM (Mapeamento Objeto-Relacional) para mapear classes Python em tabelas de banco de dados
# e facilitar operações SQL através de código orientado a objetos

from sqlalchemy import create_engine #responsável por criar a conexão com o banco de dados
from sqlalchemy.ext.declarative import declarative_base #usado para criar a classe base para os modelos ORM
from sqlalchemy.orm import sessionmaker #criar sessões de banco de dados
import pymysql # Esta importação é necessária mesmo não sendo usada diretamente

# Define a string de conexão com o banco de dados MySQL
STR_DATABASE = f"mysql+pymysql://root:password@127.0.0.1/abcBolinhas?charset=utf8mb4"

# Cria o engine (motor) de conexão com o banco de dados
# - engine é o ponto de entrada principal do SQLAlchemy para interagir com o banco
# - echo=True: ativa o modo debug, mostrando todas as queries SQL executadas no console
engine = create_engine(STR_DATABASE, echo=True)

# A sessão é usada para fazer queries, inserções, atualizações e exclusões
Session = sessionmaker(bind=engine)

# para trabalhar com tabelas
# Base será herdada por todas as classes que representam tabelas do banco de dados
Base = declarative_base()