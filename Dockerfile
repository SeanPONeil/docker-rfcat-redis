FROM seanponeil/rfcat

ENV REDIS_HOST redis
ENV REDIS_PORT 6379
ENV BIND_PORT 5000
EXPOSE $BIND_PORT

RUN apt-get update
RUN apt-get upgrade -y

WORKDIR /rfcat-redis
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD app.py .

ENTRYPOINT ["python", "app.py"]
