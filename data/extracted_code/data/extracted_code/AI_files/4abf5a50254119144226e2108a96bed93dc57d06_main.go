services:
  whatever-origin:
    image: ghcr.io/reynaldichernando/whatever-origin:latest
    ports:
      - 80:8080
    restart: always