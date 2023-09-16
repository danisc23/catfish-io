FROM python:3.11.5-slim

WORKDIR /code

RUN pip install --no-cache-dir poetry==1.6.1

VOLUME /code/catfishio
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
