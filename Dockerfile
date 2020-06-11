FROM python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--reload", "--timeout=180", "--workers=6", "--worker-tmp-dir", "/dev/shm", "--bind=0.0.0.0:80", "--chdir", "/app/itunes", "itunes.wsgi"]

