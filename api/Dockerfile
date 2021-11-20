FROM python:3.8-slim-buster

WORKDIR /app

COPY ./api/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./api .


ENV PORT 8080
ENV HOST 0.0.0.0
EXPOSE 8080
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]