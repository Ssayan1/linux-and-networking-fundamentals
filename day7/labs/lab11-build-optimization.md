# Lab 11 — Optimize Build Speed & Image Size


## 🧪 Steps


1️⃣ Enable BuildKit

```bash
export DOCKER_BUILDKIT=1
```

2️⃣ See Build Cache

```bash
docker build --progress=plain .
```

3️⃣ Compare Slim Images

```bash
docker images | grep microservices-stack
```

4️⃣ Use Multi-Stage Builds

Show improvement in:

- image size

- build time
