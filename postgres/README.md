# PostgreSQL

- https://www.postgresql.org/
- https://hub.docker.com/_/postgres
- https://github.com/docker-library/postgres

## Images

I typically don't go with `alpine` images for web app databases.

Instead, find the latest stable `bookworm` release and pin the version. Major version changes require upgrading the database, so rebuilding with `latest` can potentially cause headaches.

## Docker Secrets

- https://github.com/docker-library/docs/blob/master/postgres/README.md#docker-secrets

Open the `auth` folder and remove `.example` from the filenames.

Not ideal to store passwords in plaintext, but this is a simple example. Do not commit these files.

## Environment Variables

- https://www.postgresql.org/docs/14/libpq-envars.html
- https://github.com/docker-library/docs/blob/master/postgres/README.md#environment-variables
