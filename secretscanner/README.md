# deepfence/SecretScanner

- https://github.com/deepfence/SecretScanner
- https://registry.hub.docker.com/r/deepfenceio/deepfence_secret_scanner_ce
- https://community.deepfence.io/docs/secretscanner/

## Usage

### Scan docker image

1. Edit `./img/docker-compose.yml`
2. Replace `-image-name` value
3. Start container, attach to logs:

```
docker compose up -d && docker compose logs -f secretscanner-img
```

### Scan local directory

1. Edit `./local/docker-compose.yml`
2. Replace `/tmp` path under `volumes`
3. Start container, attach to logs:

```
docker compose up -d && docker compose logs -f secretscanner-local
```

### Cleanup

```
docker-compose down --remove-orphans
```
