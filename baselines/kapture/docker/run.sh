docker run -it --rm \
    --ipc host --net host --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --name iprofi_${USER} \
    --privileged \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v /home/${USER}/iprofihack/baselines/kapture/scripts:/home/${USER}/YaProfi:rw \
    -v /data/${USER}:/data/${USER}:rw \
    -v /data_fast/${USER}:/data_fast/${USER}:rw \
    -v /data_fast/IPROFI:/data_fast/IPROFI:ro \

    iprofi_${USER}:latest

