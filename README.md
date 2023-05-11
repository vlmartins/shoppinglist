<details> 
<summary> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg" alt="Brazilian flag" style="width:15px;height:12px;"> <span sytle="color: #0077FF;"> Em português clique aqui. </span> </summary>

# Uma lista de compras usando React FastAPI MongoDB com JWT (JSON Web Tokens) pronto para rodar online em servidores AWS EC2.

Antes de começar, você pode acessar essa aplicação live em http://54.233.129.141/ - Project 1. Você precisa registrar um usuário para acessar a aplicação. 

## Requisitos:
- MongoDB
- Docker

Se você quiser executar em sua máquina local, PRIMEIRO você precisa de uma database Mongo.

Para este exemplo, sugiro o uso do Atlas - é online e gratuito para fins de teste. Não se esqueça de alterar as configurações do firewall para incluir seu endereço IP. 

1) Renomeie /fastapi/shopconfig-sample.py para /fastapi/shopconfig.py.

2) Configure o MongoDB no arquivo shopconfig.py:

```python
MOTOR_KEY = "mongodb+srv://username:password@hostname/?retryWrites=true&w=majority"
```
Altere a variável MOTOR_KEY com seu host e senha para o seu servidor MongoDB.

3) Configure sua chave de segurança:

Crie sua própria chave para decodificar os tokens dos usuários. No Linux, digite:

```bash
openssl rand -hex 32
```
E altere a variável SECRET_KEY no arquivo shopconfig.py:

```python
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
```

4) Você precisa ter o Docker instalado para executar a linha de comando docker-compose:

```docker
docker-compose up -d --build
```

Pronto! Você está pronto para começar, verifique seu [localhost] (http://localhost/).


</details>

<br>

# A shopping list using React FastAPI MongoDB with JWT(Json Web Tokens)

Before we start, you can access this application live at http://54.233.129.141/ . You need to register a user to access the application.

This repository uses ReactJS to provide a frontend web application and FastAPI-MongoDB as a backend service that is ready to run on the cloud like AWS EC2.  

## Requirements: 
- MongoDB 
- Docker


If you want to run on your local machine FIRST you need an mongo DB server.

For this example i suggest using Atlas - It is online and free for testing purposes. Don't forget to change firewall settings to include your IP address.  


1) Rename  /fastapi/shopconfig-sample.py to /fastapi/shopconfig.py

2) Setup MongoDB in the shopconfig.py file

```python
MOTOR_KEY = "mongodb+srv://username:password@hostname/?retryWrites=true&w=majority"
```
Change the username, password and hostname to your MongoDB server.

2) Setup your security Key in the shopconfig.py file

Create your own key to decode users tokens. Add a openssl rand -hex 32. On linux type:

```bash
openssl rand -hex 32
```
Use the key to change the SECRET_KEY variable in the shopconfig.py file:

```python
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
```


3) You need Docker installed in order to run the docker-compose command line:

```docker
 docker-compose  up -d --build
```

Done! You're good to go, check your [localhost](http://localhost/)

