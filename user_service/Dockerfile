FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app/ ./app

EXPOSE 3002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3002"]
