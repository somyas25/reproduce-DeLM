FROM python:3.11-slim

WORKDIR /app

COPY human-eval/ /app/human-eval/
RUN pip install -e /app/human-eval

COPY src/ /app/src/
COPY benchmark/ /app/benchmark/
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python3", "-m", "benchmark.run"]