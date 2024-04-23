FROM python:3.10

WORKDIR /app_receipt

COPY ./requirements.txt /app_receipt/
RUN pip install --no-cache-dir --upgrade -r /app_receipt/requirements.txt

COPY ./app /app_receipt/app
COPY .env /app_receipt

COPY ./migration /app_receipt/migration
COPY ./alembic.ini /app_receipt/alembic.ini

EXPOSE  8080

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host  0.0.0.0 --port  8080"]