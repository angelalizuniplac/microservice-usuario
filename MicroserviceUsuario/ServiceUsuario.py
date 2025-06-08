import json #manipulação de dados JSON
from nameko.rpc import rpc #Importa o decorador rpc do Nameko para criar métodos de chamada remota
# Importa a extensão DatabaseSession do Nameko para gerenciar sessões de banco de dados
from nameko_sqlalchemy import DatabaseSession
from ModelUsuario import Usuario, db # Importa o modelo Usuario e a configuração do banco de dados

# Define a classe do serviço de usuários (microserviço)
class ServiceUsuario:
    # Nome identificador do serviço no cluster Nameko
    name = "service_usuario"

    # Cria uma sessão de banco de dados vinculada ao modelo SQLAlchemy
    # db.Base é a classe base que contém os metadados das tabelas
    db = DatabaseSession(db.Base)

    # Decorador @rpc transforma o método em um endpoint de chamada remota
    @rpc
    def AddUser(self, event):
        try:
            aux = json.dumps(event)  #converte 'event' para string JSON
            dados = json.loads(aux)  #desserializar a partir de uma string JSON

            # Cria uma nova instância de Usuario. Extrai 'nome' e 'email' do dicionário de dados
            user = Usuario(None, dados['nome'], dados['email'])

            # Adiciona o objeto user à sessão do banco (ainda não salva)   
            self.db.add(user)

            #salva todas as alterações pendentes no banco de dados
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

            # Atualiza os campos do usuário com os novos valores
            user.nome = dados['nome']
            user.email = dados['email']

            # Adiciona o objeto modificado à sessão
            self.db.add(user)
            # Confirma as alterações no banco
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

            # Busca o usuário existente pelo ID
            user = self.db.query(Usuario).filter(Usuario.id == dados['id']).one()
            
            # Remove o usuário do banco de dados
            self.db.delete(user)
            # Confirma as alterações no banco
            self.db.commit()

            return {'id': user.id, 'nome' : user.nome, 'email': user.email, 'msg': 'delete ok'}
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}, 400
        finally:
            self.db.close()