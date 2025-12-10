# Image Security Scanning

SREs must ensure images are free from vulnerabilities.

## Recommended Tool: Trivy

Install:
```
sudo apt install trivy -y
```

Scan an image:
```
trivy image python:3.11-slim
```

Scan your image:
```
trivy image myapp:latest
```

Outputs CVEs with severity:
- LOW
- MEDIUM
- HIGH
- CRITICAL
