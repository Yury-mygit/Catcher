# Catcher

Catcher -  application whose main function is to catch requests from a third-party server and display the request on the main page

It is used only at the development stage, to understand what request was sent by the application being developed and, if necessary, return a response to it.

While it works, it stores and show the last 10 queries in the Reddis database. Others request will be deleted

The main page shows information about the request
request body
Headings
request type, etc.

The information is displayed either in the format in which the request came, json or xml. The format is selected using the key in the upper right corner of the block in which the request is displayed.

It can respond to an incoming request either automatically, or by pressing a key, under the text of the request. You can set how you will respond. Indicates whether a response has already been sent, but can respond to the same request several times.


Desired structure.
nginx as proxy server
python django as back
reddit as db


Road map of application:
1. Setup the environment:  
#### 1.1   Make net
   
  ```bash
  docker network create -d bridge catcher_net
  ```




### 1.2   Running in docker Nginx
Creating image with definition of dockerfile

```bash
docker build -t web1 -f ${PWD}/server/nginx.dockerfile .
``` 
<p>&nbsp;</p>

#### Running a container

```bash
docker run --network catcher_net -d --name web_server `
-p 1080:80 `
-v ${PWD}/server/catcher_nginx.conf:/etc/nginx/conf.d/default.conf `
nginx
```
<p>&nbsp;</p>

Access to resources is possible

```bash
http://api.sphere.com:801/fake-users/5
```
```bash
http://sphere.com.com:801/
```

-----


<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

### 1.3   Running in docker Redis  

```bash
docker pull redis
```

```bash
docker run --name redis_for_catcher --network catcher_net -p 6379:6379 -d redis
```





### 1.4   Setup and running in docker Django  

```bash
python -m pip install Django   
```

```bash
cd catcher  
```
 
```bash
python manage.py runserver
```

```bash
docker build -t catcher -f catcher.dockerfile .
```


```bash
docker run --network catcher_net -d --name catcher `
-v ${PWD}:/code `
-v ${PWD}/requirements.txt:/code/requirements.txt `
-p 802:80 catcher
```
```bash
ALLOWED_HOSTS = ['0.0.0.0']
```
```bash
python manage.py runserver 0.0.0.0:80
```

```bash
pip install -r  requirements.txt 
```

3. Configure Nginx: Configure Nginx as a proxy server to forward requests to Django.
Create Django Application: Create a new Django application to handle incoming requests.
Handle Incoming Requests: In Django views, write a function to catch all incoming requests, extract necessary information (request body, headers, request type), and store them in Redis.
Store Requests in Redis: Use Redis as a cache to store the last 10 requests. When a new request comes in, remove the oldest one if there are already 10 requests in the cache.
Display Requests: Create a view to display the stored requests. The format of the display (JSON or XML) can be selected by a key.
Respond to Requests: Add functionality to respond to incoming requests either automatically or manually. Keep track of whether a response has been sent to a request.
Create Frontend: Create a frontend to display the requests and allow user interaction for sending responses.
Here is a simplified example of how you can implement some parts of this in Django:


### GIT

```bash
git clone git@github.com:Yury-mygit/Catcher.git
```

```bash
git add .  
```

```bash
git commit -m "first commit6"  
```

```bash
git push 
```

```bash
Pip Freeze
```

```bash
pip freeze > requirements.txt
```

```bash
pip install -r requirements.txt
```