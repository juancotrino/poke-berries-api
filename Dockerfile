# Lighter image
FROM python:3.11.1-alpine

WORKDIR /prod
COPY app app
COPY static static
COPY main.py main.py
COPY docs.py docs.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV POKE_API_URL=$POKE_API_URL
ENV REDIS_HOST=$REDIS_HOST

EXPOSE 8000

CMD ["python", "main.py"]
