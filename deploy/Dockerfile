FROM python:alpine3.22

USER root

RUN apk update && apk add --no-cache \
    pandoc \
    curl \
    tree

WORKDIR /app

# create a user
RUN adduser -D appuser && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app
USER appuser
ENV PATH="/home/appuser/.local/bin:$PATH"

# install python packages with uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
COPY pyproject.toml .

RUN uv sync

COPY . .

RUN uv run python docs_converter/godot_docs_converter.py

RUN tree docs/. > docs/docs_tree.txt

CMD ["uv", "run", "fastmcp", "run", "main.py"]
