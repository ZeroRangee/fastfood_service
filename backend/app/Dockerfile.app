FROM python:3.11-alpine3.21

WORKDIR /app



RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /app/


RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction

COPY . /app/

EXPOSE 8000

CMD [ "ls" ]

# CMD [ "poetry", 'run', 'start' ]