FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV FLASK_APP=app:create_app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
