FROM ubuntu:18.04

label version="1.1"
label description="A bot for social medias"
label author="psyduck3@protonmail.com"

RUN apt-get update && apt-get install -y curl && apt-get clean

RUN apt-get install zip -y \ 
    && apt-get install -y python3.7 \
    && apt-get install -y python3-pip \
    && apt-get install -y sqlite3 

WORKDIR /home/Projects

# RUN mkdir /home/Projects
# RUN cd /home/Projects

ENV USER psy_duck_s3
ENV SHELL /bin/bash

ARG REPO=master

RUN curl -LOk http://github.com/I-am-psy-duck/psy-bots/archive/${REPO}.zip

RUN unzip ${REPO}.zip

RUN mv psy-bots-${REPO} psy-bots

RUN pip3 install -r psy-bots/requirements.txt 
RUN touch psy-bots/database/bot.db

#RUN sqlite3 psy-bots/database/bot.db << END_SQL \
 #   .read DDL_BOTS.sql; END_SQL

CMD ["bash"] 
