# Docker Build Cache Guide

Cache hits happen when:

- A layer has the same instruction + file hash
- Build context didn't change

Example of cache-friendly Dockerfile:

```Dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

Why?
- requirements rarely change  
- app code changes often  
