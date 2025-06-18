## Gerando imagem docker e enviando para o repositorio 
1. Verifique qual ip está executando os container rabbitMQ e MySql, através dos comandos: 

```docker inspect -f "{{.NetworkSettings.IPAddress}}" rabbitmq```

``` docker inspect -f "{{.NetworkSettings.IPAddress}}" mysql```

2. Altere o localhost para os IPs correspondentes ao docker em: #config.yaml e #db.py

3. Rode o build do docker para criar a imagem
Ps: não esqueça do ponto no final . que indica que o dockerfile está no diretorio atual. 

``` docker build -t microservice_usuario .```

``` docker build -t microservice_funcoes .```

Faça autenticação local com o seu repositorio do docker hub 
```docker login --username=angeladlizuniplac```

4. Com a imagem criada, gere a tag: 

```docker tag microservice_usuario angeladlizuniplac/microservice_usuario```

```docker tag microservice_funcoes angeladlizuniplac/microservice_funcoes```

5. Faça o push das imagens para o repositorio docker: 

```docker push angeladlizuniplac/microservice_usuario```

```docker push angeladlizuniplac/microservice_funcoes```

## Baixando imagem docker do repositorio e criando container

```docker run -d -it --name serviceFuncoes angeladlizuniplac/microservice_funcoes```

```docker run -d -it --name serviceUsuario angeladlizuniplac/microservice_usuario```


## Testar 

1. Abra um dos serviços que tenha comunicação com o rabbitMQ através do comando:

```docker exec -it serviceFuncoes nameko shell --config config.yaml```

Ou terminal integrado do docker desktop. 

2. Excute os comandos RPC que desejar como por exemplo: 

>>>``` n.rpc.service_usuario.AddUser(event={'id': '0', 'nome': 'Sistemas Distribuídos', 'email': 'abc@123'})```


## Escalonamento 
1. Caso necessite subir mais de um serviço baseado na mesma imagem: 

```docker run -d -it --name serviceUsuario2 angeladlizuniplac/microservice_usuario```