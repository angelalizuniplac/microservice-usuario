# Requisitos: 

1. Baixar imagem do mySql para rodar em docker: 

    ```docker run -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 --name mysql --restart unless-stopped -d mysql:9```

Configurar a base:
2.  Usar o cliente MySQL dentro do container, no terminal execute:

```docker exec -it mysql mysql -u root -p```

3. Nesse mesmo terminal crie a tabela 'abcBolinhas:

    ```create database abcBolinhas;```

4. Baixe a imagem do RabbitMQ para rodar em docker:

 ```docker run -d --restart=always --hostname rabbitmq --name rabbitmq -p 8080:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:4.1-management-alpine```

# Ambiente virtual 
1. Criar um ambiente virtual para isolar o projeto:

    ```python -m venv venv```

2. Ativar o ambiente:

    ```venv\Scripts\activate```

3. Instalar a biblioteca Nameko e outras necessárias: 

    ```python -m pip install --upgrade pip setuptools```
    ```pip install nameko```
    ```pip install sqlalchemy```
    ```pip install nameko_sqlalchemy```
    ```pip install pymysql```
    ```pip install cryptography```

4. Atualize o arquivo de requeriments

 ```pip freeze > requirements.txt```


# Execução 
A execução precisa ser realizada através do Nameko

1. Executar através do Nameko: 
 ```nameko run ServiceUsuario --config config.yaml```

# Testes
1. Em um novo terminal, execute o comando abaixo para abrir um shell nameko (não esqueça do venv):
 ```nameko shell --config config.yaml```

2. No mesmo terminal, para fazer chamadas rcp e testar o serviço execute um por vez:

```
>>> n.rpc.service_usuario.AddUser(event={'id': '0', 'nome': 'Sistemas Distribuídos', 'email': 'abc@123'})

>>> n.rpc.service_usuario.AddUser(event={'id': '0', 'nome': 'Abc Bolinhas', 'email': 'bolinhas@123'})

>>> n.rpc.service_usuario.UpdateUser(event={'id': '2', 'nome': 'seuNome', 'email': 'seuNome@123'})

>>> n.rpc.service_usuario.DeleteUser(event={'id': '1'})

>>> n.rpc.service_usuario.GetUser(event={'id': '2'})

>>> n.rpc.service_usuario.GetUser(event={'id': '1'}) 
```