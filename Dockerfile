FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Use gunicorn for production-like serving
CMD ["gunicorn", "-b", "0.0.0.0:5000", "flask_demo:app"]

