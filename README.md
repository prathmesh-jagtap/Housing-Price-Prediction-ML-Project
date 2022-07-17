# Machine-Learning-Project

Machine Learning Deploy link:
[Housing Price Predictor](https://ml-regressor-app.herokuapp.com/)

### Creating conda Environment

```
conda create -p venv python==3.7 -y
```

```
conda activate venv
```

```
pip install -r requirements.txt
```

Now to Add files from terminal use:

```
git add .
```

or

```
git add <file name>
```

To check all versions maintained by git

```
git log
```

To create or update version/commit all changes by git

```
git commit -m "<message>"
```

To send or save verison/changes to GitHub

```
git push origin main or git push
```

To check remote url

```
git remote -u
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = < jagtaprathmesh19@gmail.com >
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME =

Build Docker Image

```
docker build -t <image_name>:<tagname> .
```

> Note: Image name for docker must be lowercas

To list out docker images

```
docker images
```

Run docker image

```
docker run -p 5000:5000 -e PORT=5000 187e678ae51c
```

To check running container in docker

```
docker ps
```

Tos stop docker conatiner

```
docker stop <container_id>
```

```
python setup.py install
```

Install ipykernel

```
pip install ipykernel
```
