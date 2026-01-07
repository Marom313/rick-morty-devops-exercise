FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

# create output dir inside container
RUN mkdir -p /app/output

CMD ["python", "src/export_characters.py"]
