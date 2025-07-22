FROM python:alpine3.22

USER root

RUN apk update && apk add --no-cache \
    pandoc \
    curl

COPY . /app

WORKDIR /app

RUN adduser -D appuser && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app

USER appuser

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH" && \
    source $HOME/.local/bin/env

RUN uv sync && source .venv/bin/activate

RUN python docs_converter/godot_docs_converter.py

CMD ["python", "server.py"]
