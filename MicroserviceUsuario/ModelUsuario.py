# Importa os componentes necessários do SQLAlchemy para definir colunas e tipos de dados
from sqlalchemy import Column, Integer, VARCHAR
import db #contém a configuração do banco de dados - arquivo criado por nós

# Define a classe Usuario que herda de db.Base (classe base do SQLAlchemy)
# Esta herança transforma a classe em um modelo de tabela do banco de dados
class Usuario(db.Base):
    __tablename__ = "tb_usuario" #nome da tabela

    id = Column(Integer,primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False)

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

# Executa a criação da tabela no banco de dados
# db.Base.metadata: contém informações sobre todas as tabelas definidas
# create_all(): comando para criar todas as tabelas especificadas
# db.engine: conexão com o banco de dados
# tables=[Usuario.__table__]: especifica que apenas a tabela Usuario deve ser criada
db.Base.metadata.create_all(db.engine, tables=[Usuario.__table__])