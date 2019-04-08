FROM python:3.6.4-slim

# author
MAINTAINER Ahmed Kammorah


RUN apt-get update -y
RUN apt-get install python-dev -y
RUN pip install -U setuptools

RUN python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80 8000 5000 5005

# cd on this dir 
COPY . /app
WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:/app/MainService
ENV AKSERVICE=/app/MainService

# Start With entryPoint 
COPY ./docker-entrypoint.sh /
RUN chmod 771 /docker-entrypoint.sh

# main command when Run new container from The Image
CMD ["/bin/bash"]

#ENTRYPOINT ["/docker-entrypoint.sh"]


