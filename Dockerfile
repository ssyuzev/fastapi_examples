FROM tiangolo/uvicorn-gunicorn:python3.11

ENV PYTHONUNBUFFERED=1
ENV  PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
EXPOSE 80

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src /app
RUN chmod +x wait-for-it.sh

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
