# Docker Image Layers Explained

Every Dockerfile instruction creates a layer.

Example:

```Dockerfile
FROM python:3.11-slim   # LAYER 1
COPY . /app              # LAYER 2
RUN pip install -r ...   # LAYER 3
CMD ["python", "app.py"] # LAYER 4
```

## Analyze Layers

```
docker history myimage
```

## Why layers matter?

- Cache reuse  
- Faster builds  
- Smaller images  
- Efficient CI/CD  
- Less storage required  
