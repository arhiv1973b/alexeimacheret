FROM alpine:3.18
LABEL maintainer='A©tor'
WORKDIR /app
COPY . /app
CMD ["sh", "-c", "echo 'Hooper node ready: TI-ULA_AUTH'; sleep infinity"]
