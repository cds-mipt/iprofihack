docker build .. \
    -f Dockerfile \
    --build-arg UID=$(id -g) \
    --build-arg GID=$(id -g) \
    -t iprofi_${USER}:latest

