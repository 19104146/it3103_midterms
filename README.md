# IT 3103 - Midterms

## Prerequisites

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/19104146/it3103_exercise3.git
   ```

2. Navigate to the project directory:

   ```bash
   cd it3103_exercise3
   ```

3. Define the JWT_SECRET environment variable:

   ```bash
   echo "JWT_SECRET=$(openssl rand -hex 32)" > .env
   ```

4. Start the project:

   ```bash
   docker-compose up --build -d
   ```

5. To stop the project:
   ```bash
   docker-compose down
   ```
