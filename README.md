# Flask and Python 3 docker container

## Build it

```
docker build -t flask-python-sample:latest .
```

Or with docker-compose

```
docker-compose build
```

## Run it

```
docker run -d -p 5000:5000 flask-python-sample
```

Or with docker-compose

```
docker-compose up -d
```

## Access to the shell

```
docker exec -ti flask-python-sample /bin/bash
```

### Note

If you use docker-compose, you can do live changes

## See it in action

Go to `http://localhost:5000` and you should see flask running :-)