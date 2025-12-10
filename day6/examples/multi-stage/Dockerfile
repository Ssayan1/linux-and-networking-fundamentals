FROM python:3.11 AS builder
WORKDIR /app
COPY app.py .
RUN echo "Build stage complete"

FROM python:3.11-slim
COPY --from=builder /app/app.py /app/app.py
CMD ["python", "/app/app.py"]
