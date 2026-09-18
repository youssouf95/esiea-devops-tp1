FROM python:3.12

WORKDIR /app

RUN useradd --create-home appuser

COPY --chown=appuser:appuser . .

RUN pip install -r requirements.txt

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
