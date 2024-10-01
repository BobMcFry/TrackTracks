FROM python:3.12.2-slim-bookworm as builder
# Install uv for dependency intallation
COPY --from=ghcr.io/astral-sh/uv:0.4.17 /uv /bin/uv

# Change the working directory to the `app` directory
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Copy the project into the intermediate image
ADD . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

FROM python:3.12.2-slim-bookworm

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Dependencies: qreader->libzbar0 (we need an update for that)
RUN apt update && apt install -y libzbar0 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the environment, but not the source code
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY . /app
WORKDIR /app

# Run the application.
CMD echo "Inject command"
