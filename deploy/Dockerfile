FROM python:alpine3.22

USER root

RUN apk update && apk add --no-cache \
    pandoc \
    curl \
    tree

COPY . /app

WORKDIR /app

RUN adduser -D appuser && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app

USER appuser

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

ENV PATH="/home/appuser/.local/bin:$PATH"

RUN uv sync

RUN uv run python docs_converter/godot_docs_converter.py

RUN tree docs/. > docs/docs_tree.txt

CMD ["uv", "run", "fastmcp", "run", "main.py"]
