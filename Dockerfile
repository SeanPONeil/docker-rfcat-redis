FROM seanponeil/rfcat

RUN apt-get update
RUN apt-get upgrade -y

WORKDIR /rfcat-redis
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD app.py .

ENTRYPOINT ["python", "app.py"]
