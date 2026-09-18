FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt


FROM python:3.12-slim

WORKDIR /app

RUN useradd --create-home appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser app.py .

ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind=0.0.0.0:5000", "app:app"]
