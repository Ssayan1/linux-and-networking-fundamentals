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

## 📘 How Docker Image Layers Work (ASCII Diagram)

```
+-------------------------------+
|        Final Image            |
| (Flattened stack of layers)   |
+-------------------------------+
            ▲
            |
+-------------------------------+
| CMD / ENTRYPOINT Layer        |
+-------------------------------+
            ▲
+-------------------------------+
| Application Code Layer        |
|  COPY . /app                  |
+-------------------------------+
            ▲
+-------------------------------+
| Dependencies Layer            |
|  RUN pip install / npm ci     |
+-------------------------------+
            ▲
+-------------------------------+
| Base Layer (python:3.11-slim) |
+-------------------------------+

```


### Layer Rules
- Layers are immutable  
- Only changed layers rebuild  
- Ordering matters for caching  
- Multi-stage builds produce cleaner final layers
