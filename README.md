# "React Fast/API MongoDB JWT Access Web APP with Cookies"

This repository uses ReactJS to provide a frontend web application and FastAPI-MongoDB as a backend service.  

If you want to run on your local machine FIRST you need an mongo DB server.

1) For this example i suggest using Atlas - It is free for testing purposes.  

Once you create your account you have to edit database.py and insert your key on line 6, like this:

```python
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://youraccount:<password>@cluster.ffasda1.mongodb.net/?retryWrites=true&w=majority")
```

Change firewall settings to include your IP address.  


2) Create your own key to decode users tokens. Add a openssl rand -hex 32. On linux type:

```bash
openssl rand -hex 32
```
Edit main.py line 23 and add the secre_key value like as it follows:

```python
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
```


3) You need Docker installed to run the docker-compose command line:

```docker
 docker-compose  up -d --build
```

Done! You're good to go, check your [localhost](http://localhost/)