FROM python:3.11.5-slim

WORKDIR /code

RUN pip install --no-cache-dir poetry==1.6.1

COPY catfishio /code/catfishio
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi
