FROM seanponeil/rfcat

RUN apt-get update
RUN apt-get upgrade -y

WORKDIR /tmp
ADD requirements.txt .
RUN pip install -r requirements.txt


