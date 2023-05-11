<details> 
<summary> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg" alt="Brazilian flag" style="width:15px;height:12px;"> <span sytle="color: #0077FF;"> Em português clique aqui. </span> </summary>

# Uma lista de compras usando React FastAPI MongoDB com JWT (JSON Web Tokens)

Antes de começar, você pode acessar essa aplicação live em http://54.233.129.141/ - Projeto um

Este repositório utiliza ReactJS como uma aplicação web front-end e o FastAPI-MongoDB como serviço back-end.

Requisitos:
- MongoDB
- Docker

Se você quiser executar em sua máquina local, PRIMEIRO você precisa de um servidor MongoDB.

Para este exemplo, sugiro o uso do Atlas - é gratuito para fins de teste. Não se esqueça de alterar as configurações do firewall para incluir seu endereço IP.

1) Renomeie /fastapi/shopconfig-sample.py para /fastapi/shopconfig.py.

2) Configure o MongoDB no arquivo shopconfig.py:

```python
MOTOR_KEY = "mongodb+srv://username:password@hostname/?retryWrites=true&w=majority"
```
Altere o nome de usuário, a senha e o nome do host para o seu servidor MongoDB.

3) Configure sua chave de segurança no arquivo shopconfig.py:

Crie sua própria chave para decodificar os tokens dos usuários. Adicione um "openssl rand -hex 32". No Linux, digite:

```bash
openssl rand -hex 32
```

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



This repository uses ReactJS to provide a frontend web application and FastAPI-MongoDB as a backend service.  

Requirements: 
- MongoDB 
- Docker


If you want to run on your local machine FIRST you need an mongo DB server.

For this example i suggest using Atlas - It is free for testing purposes. Don't forget to change firewall settings to include your IP address.  


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

```python
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
```


3) You need Docker installed to run the docker-compose command line:

```docker
 docker-compose  up -d --build
```

Done! You're good to go, check your [localhost](http://localhost/)

