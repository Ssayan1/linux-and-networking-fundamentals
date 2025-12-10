# LAB 3 — Multi Stage Build

1. Build multi-stage image:

```
cd day6/examples/multi-stage
docker build -t multiapp .
```

2. Compare size:

```
docker images | grep multiapp
```
