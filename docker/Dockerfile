FROM python:3.9-slim

WORKDIR /app

COPY docker/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

ENV PYTHONPATH="/app/src"

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "src.run:app"]
