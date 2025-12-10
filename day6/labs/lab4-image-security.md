# LAB 4 — Image Security Scanning

1. Scan base image:

```
trivy image python:3.11-slim
```

2. Scan your built image:

```
trivy image python-hello
```

3. Document all:
- CRITICAL CVEs  
- HIGH CVEs  
- Fix steps  
