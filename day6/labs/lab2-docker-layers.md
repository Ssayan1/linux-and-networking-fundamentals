# LAB 2 — Analyze Image Layers

1. Build the image:

```
docker build -t layer-test .
```

2. Inspect layers:

```
docker history layer-test
```

3. Inspect image metadata:

```
docker inspect layer-test
```
