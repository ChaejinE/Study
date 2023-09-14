FROM nginx:latest

RUN apt-get update
RUN apt-get install -y vim systemd curl
USER root
RUN chmod 777 /etc/hosts && echo "127.0.0.1 helloworld.com" >> /etc/hosts
