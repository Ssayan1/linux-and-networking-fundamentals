# Dockerfile Best Practices

## 1. Use small base images
Prefer:
- `python:3.11-slim`
- `alpine`
- `debian-slim`

## 2. Minimize layers
Combine RUN commands:

```Dockerfile
RUN apt update && \
    apt install -y curl && \
    rm -rf /var/lib/apt/lists/*
```

## 3. Avoid root user

```Dockerfile
USER appuser
```

## 4. Use `.dockerignore`

Example:

```
__pycache__/
*.log
.env
.git/
```

## 5. Leverage build cache
Order instructions from stable → changing.
