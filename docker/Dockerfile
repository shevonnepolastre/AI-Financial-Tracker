FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code as a package
COPY src/app ./app
COPY run.py .

EXPOSE 8000

# Run Waitress, calling create_app() in run.py
CMD ["waitress-serve", "--listen=0.0.0.0:8000", "--call", "run:create_app"]
