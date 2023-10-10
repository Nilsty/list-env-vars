FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
