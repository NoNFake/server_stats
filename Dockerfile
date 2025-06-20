FROM python:3.13-alpine  

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r req.txt

CMD ["python", "main.py"]