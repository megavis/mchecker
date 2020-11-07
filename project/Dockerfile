FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip && \
    pip install Django==3.1.3

WORKDIR /app

CMD ["python","./manage.py","runserver","0:8000"]

