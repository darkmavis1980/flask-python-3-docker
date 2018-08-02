# Flask and Python 3.7 docker container

## Build it

```
docker build -t flask-python-sample:latest .
```

## Run it

```
docker run -d -p 5000:5000 flask-python-sample
```

## See it in action

Go to `http://localhost:5000` and you should see flask running :-)