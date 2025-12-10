# Alpine vs Debian Image Size

| Image | Size |
|-------|------|
| python:3.11-alpine | ~50MB |
| python:3.11-slim | ~130MB |

Alpine is smaller but may break:
- pip installs (musl vs glibc issues)
- compiled extensions
