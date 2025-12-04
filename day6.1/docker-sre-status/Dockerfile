# Stage 1: base image (we keep it single-stage for now, but SRE-ready)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Avoid writing .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements and install (even if empty now)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Create non-root user
RUN useradd -r -s /usr/sbin/nologin sreuser

# Use non-root user
USER sreuser

# Expose port
EXPOSE 8000

# Entrypoint and default command
WORKDIR /app
ENTRYPOINT ["python", "-m", "app.main"]
