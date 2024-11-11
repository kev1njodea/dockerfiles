# kev1njodea/dockerfiles/traefik

- https://traefik.io/
- https://hub.docker.com/_/traefik
- https://github.com/traefik/traefik
- https://doc.traefik.io/traefik/
- https://doc.traefik.io/traefik/user-guides/docker-compose/basic-example/

## Overview

> Traefik (pronounced traffic) is a modern HTTP reverse proxy and load balancer that makes deploying microservices easy.

This setup provides a basic configuration of Traefik with the following features:

- **HTTPS**: Secure services with SSL/TLS.
- **Dashboard**: Built-in monitoring and management.
- **Basic Auth**: Username/password protection for the dashboard.
- **Manual SSL**: Custom certificate management.
- **Dynamic Config**: Flexible routing via Docker and file providers.
- **Auto Updates**: Watchtower for container updates.

## Getting Started

### Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Domain Name**: A registered domain name (e.g., `traefik.yourdomain.com`) pointing to your server's IP address.
- **SSL Certificates**: SSL/TLS certificates for your domain. You can obtain free certificates from [Let's Encrypt](https://letsencrypt.org/) or use your own.

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/kev1njodea/dockerfiles.git
    cd dockerfiles/traefik
    ```

2. **Configure Basic Authentication**

    Protect the Traefik dashboard by setting up basic authentication.

  - **Install `htpasswd` Utility**

    If you don't have the `htpasswd` utility, install it using:

    ```bash
    # For Debian/Ubuntu
    sudo apt-get install apache2-utils

    # For macOS using Homebrew
    brew install httpd
    ```

  - **Create `.htpasswd` File**

    Generate a `.htpasswd` file with your desired username and password:

    ```bash
    mkdir -p auth
    htpasswd -c ./auth/.htpasswd yourusername
    ```

    You'll be prompted to enter and confirm a password. This file will be used by Traefik to authenticate access to the dashboard.

3. **Install SSL Certificates**

    Manually manage your SSL certificates by placing them in the designated directory.

    Place your SSL certificate and key files in the `files/certs` directory. Ensure the filenames match those expected in your Traefik configuration (e.g., `certs.crt` and `certs.key`).

    ```yaml
    files/
      certs/
        certs.crt
        certs.key
    ```

    > **Note**: Replace `certs.crt` and `certs.key` with your actual certificate and key filenames if they differ.

4. **Create traefik-proxy network**

    ```bash
    docker network create traefik_proxy
    ```

5. **Start Traefik Container**

    Launch Traefik using Docker Compose:

    ```bash
    docker compose up -d
    ```

6. **Access the Traefik Dashboard**

    Open your web browser and navigate to:

    ```
    https://traefik.yourdomain.com/dashboard
    ```

    Enter the username and password you set up in the `.htpasswd` file to access the dashboard.

## Key Configuration Areas

1. **Entrypoints**:
   - **web**: Listens on port `80` for HTTP traffic.
   - **web-secure**: Listens on port `443` for HTTPS traffic.

2. **Providers**:
   - **Docker**: Allows Traefik to automatically detect and configure routes based on Docker containers.
   - **File**: Enables loading additional static configurations from the `/cfg/` directory.

3. **Dashboard**:
   - Accessible via `https://traefik.yourdomain.com/dashboard`.
   - Protected with basic authentication using the `.htpasswd` file.
   - Uses TLS to secure the dashboard interface.

4. **Middleware**:
   - **https-redirect**: Redirects all HTTP requests to HTTPS.
   - **auth**: Applies basic authentication to secure the dashboard.

5. **Watchtower Integration**:
   - The label `com.centurylinklabs.watchtower.enable=true` enables Watchtower to monitor and update the Traefik container automatically when new images are available.

## Proxying Additional Services

To proxy additional containers through Traefik, you need to configure each service with appropriate labels and ensure they are connected to the Traefik network.

### Prerequisites

- **External Proxy Network**: Ensure that the Traefik proxy network (`traefik_proxy`) is created. This network allows Traefik to communicate with other containers.

### Step-by-step Instructions

1. **Define the Service in Docker Compose**

    ```yaml
    container_name: container1
     restart: always
     networks:
       - traefik_proxy
     ...
    ```

2. **Connect the Service to the Traefik Network**

    ```yaml
    networks:
      traefik_proxy:
        external: true
    ```

3. **Configure Traefik Labels**

    ```yaml
      labels:
        - "traefik.http.routers.container1.rule=Host(`app.container1.xyz`)"
        - "traefik.http.routers.container1.entrypoints=web-secure"
        - "traefik.http.routers.container1.tls=true"
        - "traefik.http.routers.container1.service=container1"
        - "traefik.http.services.container1.loadbalancer.server.port=8080"
        - "traefik.http.services.container1.loadbalancer.server.scheme=http"
    ```

## Troubleshooting

- **Dashboard Not Accessible**:
  - Ensure the `.htpasswd` file is correctly placed in the `./auth` directory.
  - Verify that your domain name points to the correct server IP.
  - Check Traefik container logs for errors:

    ```bash
    docker logs <traefik-container-name>
    ```

- **SSL Certificate Issues**:
  - Confirm that the SSL certificate and key files are correctly named and placed in the `./files/certs` directory.
  - Ensure the certificates are valid and not expired.

## License

MIT. See [LICENSE](./LICENSE) for details.
