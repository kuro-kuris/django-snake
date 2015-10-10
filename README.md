# django-snake
django snake

## Setup on ubuntu:

```
virtualenv -p python3 venv
```
Activate venv:
```
. venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```

Update requirements:
```
pip freeze > requirements.txt
```

Setup environment variables:

### In a shell, set env variables
```
RBS_OBP_CLIENT_KEY='yourvalue'
export RBS_OBP_CLIENT_KEY
RBS_OBP_CLIENT_SECRET='yourvalue'
export RBS_OBP_CLIENT_SECRET
```

Check if they work:
```
printenv | grep RBS_OBP_CLIENT_KEY
printenv | grep RBS_OBP_CLIENT_SECRET
```
