FROM python:3.7-alpine

LABEL maintainer "ivam=nvernichenko@gmail.com"

WORKDIR /usr/src/mchecker

RUN apk --no-cache add wget
RUN wget https://raw.githubusercontent.com/megavis/mchecker/master/mchecker.py

#CMD ["python","./mchecker"]

#COPY ./mchecher.py /usr/src/mchecker/

