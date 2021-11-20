FROM python:3.8-slim-buster

WORKDIR /app

COPY ./api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./api .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]