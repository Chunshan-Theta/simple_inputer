FROM python:3.7

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt


EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]