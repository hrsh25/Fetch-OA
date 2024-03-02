FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 80

CMD ["python", "server.py"]
