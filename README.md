# IT 3103 - Midterms

## Prerequisites

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [mkcert](https://github.com/FiloSottile/mkcert)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/19104146/it3103_exercise3.git
   cd it3103_exercise3
   ```

2. Set up environment:

   ```bash
   echo "JWT_SECRET=$(openssl rand -hex 32)" > .env
   ```

3. Configure SSL/TLS:
   ```bash
   mkcert -install
   mkdir -p certs
   mkcert -key-file certs/key.pem -cert-file certs/cert.pem localhost 127.0.0.1
   ```

## Usage

1. Start the project:

   ```bash
   docker-compose up --build -d
   ```

   The API Gateway will be available at `https://localhost` or `https://localhost:443`.

2. Stop the project:
   ```bash
   docker-compose down
   ```
