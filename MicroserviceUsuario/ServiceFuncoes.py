import json, re
from nameko.rpc import rpc
 
class ServiceFuncoes:
    name = "service_funcoes"

    # expressão regular para validar um e-mail
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    @rpc
    def ValidaEmail(self, event):
        aux = json.dumps(event)
        dados = json.loads(aux)     
    
        if(re.fullmatch(self.regex, dados['email'])):
            return True
        else:
            return False
