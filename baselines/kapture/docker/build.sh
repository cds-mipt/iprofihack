docker build .. \
    -f Dockerfile \
    --build-arg UID=$(id -g) \
    --build-arg GID=$(id -g) \
    --build-arg USER=${USER} \
    -t iprofi_${USER}:latest

