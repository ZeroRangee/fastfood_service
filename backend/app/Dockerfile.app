FROM python:3.13-alpine3.21

WORKDIR /app

RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev


RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /app/


RUN poetry config virtualenvs.create false && \
    poetry install --no-root




COPY . .

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000


CMD ["poetry","run","start"]