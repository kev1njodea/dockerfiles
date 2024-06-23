# kev1njodea/dockerfiles

Starter Docker Compose files I've made for various self-hosted applications. Some eventually become full projects, while others are useful references or simple demos. 🐋

## System

```
Docker Engine x86_64
Docker Compose v2
VSCode + Docker extension
```

- **All docs are written for Docker Engine / CLI**
- Currently using Ubuntu 22.04, 24.04, and Amazon Linux 2023
  - Look out for any OS specific notes
  - Always using latest releases
- Can't guarantee everything works on ARM based machines

## Preferences

- `docker-compose.yml` for everything, if possible
- Consistent code layout, structure, and naming patterns
- No hard coded secrets
- Run as non-root user
- Bind Mounts (some volumes)
- Traefik Reverse Proxy
- Include configuration without proxy
- Use environment variables, and labels
- Separate `.gitignore` files within directories
- Continue to learn and implement best practices
- Document
