# uses ubuntu 18.04 as base image
FROM ubuntu:18.04

LABEL version="1.1"
LABEL description="A bot for social medias"
LABEL author="psyduck3@protonmail.com"

# update the system, install curl
RUN apt-get update && apt-get install -y curl && apt-get clean

# install python, pip, zip and sqlite3
RUN apt-get install zip -y \ 
    && apt-get install -y python3.7 \
    && apt-get install -y python3-pip \
    && apt-get install -y sqlite3 

# download google chrome deb package
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# creates the workdir, for the project
WORKDIR /home/Projects

# creates environment variables
ENV USER psy_duck_s3
ENV SHELL /bin/bash

# the base branch
ARG BRANCH=master

# project directory
ARG BASE_NAME=psy-bots

# the name of the bot database
ARG BOT_DATABASE=bot.db

# download the repository
RUN curl -LOk http://github.com/I-am-psy-duck/psy-bots/archive/${BRANCH}.zip

# unzip the repository
RUN unzip ${BRANCH}.zip

# rename the repostory 
RUN mv psy-bots-${BRANCH} ${BASE_NAME}

# install the requirements to run
RUN pip3 install -r ${BASE_NAME}/requirements.txt 

# creates a sqlite file to store the bot credentials
RUN touch ${BASE_NAME}/database/${BOT_DATABASE}

# execute a sql script to generate the tables
RUN sqlite3 ${BASE_NAME}/database/${BOT_DATABASE} < ${BASE_NAME}/database/DDL_BOTS.sql

# delete the zip 
RUN rm -Rf ${BRANCH}.zip

CMD ["/bin/bash" ] 
