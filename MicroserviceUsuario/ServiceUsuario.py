import json #manipulação de dados JSON
#Importa o decorador rpc do Nameko para criar métodos de chamada remota

from nameko.rpc import rpc, RpcProxy #NOVO RpcProxy classe do Nameko para fazer chamadas remotas para outros microserviços

from nameko_sqlalchemy import DatabaseSession # Importa a extensão DatabaseSession do Nameko para gerenciar sessões de banco de dados
from ModelUsuario import Usuario, db # Importa o modelo Usuario e a configuração do banco de dados
# import time

# Define a classe do serviço de usuários (microserviço)
class ServiceUsuario:
    # Nome identificador do serviço no cluster Nameko
    name = "service_usuario"
    serviceFuncoes = RpcProxy("service_funcoes") #NOVO Chamada remota para outro serviço como se estivesse local

    # Cria uma sessão de banco de dados vinculada ao modelo SQLAlchemy    
    db = DatabaseSession(db.Base) # db.Base é a classe base que contém os metadados das tabelas

    # Decorador @rpc transforma o método em um endpoint de chamada remota
    @rpc
    def AddUser(self, event):
        try:
            # time.sleep(5)
            aux = json.dumps(event)  #converte 'event' para string JSON
            dados = json.loads(aux)  #desserializar a partir de uma string JSON

            #NOVO faz a chamada remota para o serviço passando o email e se retornar false lança execption e se retornar false nada acontece e segue para o save
            if ( not self.serviceFuncoes.ValidaEmail({'email': dados['email']}) ):
                raise Exception({'msg': 'email inválido'})

            # Cria uma nova instância de Usuario. Extrai 'nome' e 'email' do dicionário de dados
            user = Usuario(None, dados['nome'], dados['email'])

            self.db.add(user)

            self.db.commit()

            return {'id': user.id, 'nome' : user.nome, 'email': user.email, 'msg': 'insert ok'}
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}
        finally:
            self.db.close()

    @rpc
    def GetUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)
            
            # Executa uma consulta no banco de dados
            # .one() retorna exatamente um resultado (erro se não encontrar ou encontrar múltiplos)
            user = self.db.query(Usuario).filter(Usuario.id == dados['id']).one()
            
            return {'id': user.id, 'nome' : user.nome, 'email': user.email, 'msg': 'get ok'}
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}
        finally:
            self.db.close()

    @rpc
    def UpdateUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)

            # Busca o usuário existente pelo ID
            user = self.db.query(Usuario).filter(Usuario.id == dados['id']).one()

            user.nome = dados['nome']
            user.email = dados['email']

            self.db.add(user)
            self.db.commit()

            return {'id': user.id, 'nome' : user.nome, 'email': user.email, 'msg': 'update ok'}
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}, 400
        finally:
            self.db.close()

    @rpc
    def DeleteUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)

            user = self.db.query(Usuario).filter(Usuario.id == dados['id']).one()
            
            self.db.delete(user)
            self.db.commit()

            return {'id': user.id, 'nome' : user.nome, 'email': user.email, 'msg': 'delete ok'}
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}, 400
        finally:
            self.db.close()