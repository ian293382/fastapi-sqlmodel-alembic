FROM python:3.11-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        netcat gcc postgresql default-libmysqlclient-dev libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]