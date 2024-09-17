FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -U pip wheel && pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]