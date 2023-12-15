# list-env-vars

## run local
```
uvicorn main:app --reload
```
This exposes the app on http://localhost:8000

## build container
```
docker build -t "list-env-vars" .
```

## run container
```
docker run -p 8000:8000 docker.io/library/list-env-vars
```

adding a test change
