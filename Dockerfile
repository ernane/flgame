# docker build --no-cache -t ejjunior/flgame:latest .
# docker run --rm -it -p 5000:5000 -e FLASK_SECRET_KEY=SECRET_001 ejjunior/flgame gunicorn --bind "0.0.0.0:5000" --preload "flgame.app:create_app()" 

FROM python:3.7-buster

RUN mkdir /code
WORKDIR /code

COPY requirements.txt settings.toml .flaskenv ./
RUN pip install -r requirements.txt

COPY flgame flgame/

EXPOSE 5000

# gunicorn -b 0.0.0.0:5000 --preload "flgame.app:create_app()" 
# gunicorn -b 0.0.0.0:5000 "flgame.app:create_app()" 
# gunicorn --bind "0.0.0.0:$PORT" "flapp.app:create_app()"