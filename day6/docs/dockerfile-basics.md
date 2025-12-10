# Dockerfile Basics

A Dockerfile is a set of instructions used to build a container image.

## Common Instructions

| Instruction | Purpose |
|------------|----------|
| `FROM` | Base image |
| `COPY` | Copy files into image |
| `RUN` | Execute commands at build time |
| `CMD` | Default command |
| `ENTRYPOINT` | Main executable |
| `ENV` | Environment variables |
| `WORKDIR` | Working directory |
| `EXPOSE` | Exposed ports |
| `USER` | Set non-root user |

## Example

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```
