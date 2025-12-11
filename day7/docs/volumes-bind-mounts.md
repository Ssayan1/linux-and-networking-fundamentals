# Volumes & Bind Mounts

## Named Volume
Persistent data managed by Docker.

```yaml
volumes:
  db-data:

services:
  redis:
    volumes:
      - db-data:/data

``


## Bind Mount
Maps a host directory into container.

```bash
volumes:
  - ./app:/app

```

Use bind mounts during development, volumes in production.
