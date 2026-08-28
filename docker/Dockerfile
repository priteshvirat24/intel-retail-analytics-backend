FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency definition
COPY pyproject.toml /app/

# Install python dependencies
RUN pip install --upgrade pip && \
    pip install . && \
    pip install playwright && \
    playwright install-deps chromium && \
    playwright install chromium

# Copy application source code and configurations
COPY config/ /app/config/
COPY app/ /app/app/
COPY orchestrator/ /app/orchestrator/
COPY tests/ /app/tests/

# Create runtime directories
RUN mkdir -p /app/evidence /app/reports

ENTRYPOINT ["python", "-m", "orchestrator"]
CMD ["test-all", "--limit", "20"]
