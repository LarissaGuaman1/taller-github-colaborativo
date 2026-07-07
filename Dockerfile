FROM python:3.12-slim

WORKDIR /app

LABEL org.opencontainers.image.source="https://github.com/LarissaGuaman1/taller-github-colaborativo"
LABEL org.opencontainers.image.description="Taller colaborativo con Python, GitHub Actions y Pull Requests"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY tests ./tests

ENV PYTHONPATH=/app

CMD ["python", "-m", "pytest", "-v"]