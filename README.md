# "React Fast/API MongoDB JWT Access Web APP with Cookies"

This repository uses ReactJS to provide a frontend web application and FastAPI-MongoDB as a backend service.  

Requirements: 
- MongoDB 

If you want to run on your local machine FIRST you need an mongo DB server.

For this example i suggest using Atlas - It is free for testing purposes. Don't forget to change firewall settings to include your IP address.  


1) Copy shopconfig-sample.py to shopconfig.py

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