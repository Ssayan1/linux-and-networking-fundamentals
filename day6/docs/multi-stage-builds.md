# Multi-stage Builds

Used to make images smaller by compiling in one stage and copying only the binary into the final stage.

## Example

```Dockerfile
FROM python:3.11 AS builder
WORKDIR /app
COPY . .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /root/.local /root/.local
COPY app.py /app/app.py
CMD ["python", "/app/app.py"]
```

Benefits:
- Smaller image size  
- No build tools in final image  
- Fewer attack surface
