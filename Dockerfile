FROM python:3.10-alpine

EXPOSE 8000
WORKDIR /app
CMD ["uvicorn", "cli:app", "--host", "0.0.0.0", "--port", "8000"]

COPY pyproject.toml .

RUN apk add --update --no-cache --virtual .tmp-build-deps build-base python3-dev libffi-dev coreutils openssl-dev && \
    pip install --no-cache-dir -U pip poetry && \
    poetry config virtualenvs.create false --local && \
    poetry env use system && \
    poetry install --no-dev && \
    apk del .tmp-build-deps && \
    rm -rf /root/.cache

COPY app /app

ARG VERSION
ENV VERSION=$VERSION
