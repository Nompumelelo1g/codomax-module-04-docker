# Module 4: Docker & Containerization

## Project Overview

This project demonstrates how to containerize a simple Python Flask web application using Docker and Docker Compose.

The application displays a message, reads an environment variable, and saves and retrieves data using a Docker named volume.

## Technologies Used

- Python 3.12
- Flask
- Docker Engine
- Dockerfile
- Docker Compose

## Project Structure

```text
docker-webapp/
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
└── README.md
```

## Application Features

- Displays a message on the home page.
- Uses the `APP_MESSAGE` environment variable.
- Saves data to `/data/test.txt`.
- Reads saved data from the Docker volume.

## Docker Concepts Demonstrated

### 1. Docker Image

The Dockerfile defines how the application image is built.

Build the image:

```bash
sudo docker build -t docker-webapp .
```

### 2. Docker Container

A container runs the application using the built image.

### 3. Port Mapping

The application listens on port 5000 inside the container. Port 8080 on the host is mapped to it.

### 4. Environment Variables

The application reads `APP_MESSAGE` to display a configurable message.

### 5. Docker Volumes

A named volume called `app-data` is mounted at `/data`.

The `/save` and `/read` endpoints demonstrate writing and retrieving persistent data.

### 6. Docker Compose

Compose manages the application service, port mapping, environment variable and named volume.

Start the application:

```bash
sudo docker compose up -d --build
```

Stop and remove the container and network:

```bash
sudo docker compose down
```

The named volume is preserved when `docker compose down` is run without `-v`.

## Accessing the Application

Open:

http://localhost:8080

Available endpoints:

| Endpoint | Purpose |
|---|---|
| `/` | Displays the application message |
| `/save` | Saves data to the named volume |
| `/read` | Reads saved data from the volume |

## Useful Docker Commands

```bash
sudo docker images
sudo docker ps
sudo docker compose ps
sudo docker volume ls
sudo docker network ls
sudo docker compose logs
```

## Conclusion

This project demonstrates the fundamentals of Docker containerization, including images, containers, Dockerfiles, port mapping, environment variables, networking, persistent storage and Docker Compose.
