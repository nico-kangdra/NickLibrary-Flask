FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN cp .env.example .env

EXPOSE 3000

CMD ["python3", "app.py"]