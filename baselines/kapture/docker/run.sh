docker run -it --rm \
    --ipc host --net host --gpus all -e NVIDIA_DRIVER_CAPABILITIES=all \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --name iprofi_${USER} \
    --privileged \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v /home/yaprofi2021/${USER}/iprofihack/baselines/kapture/scripts:/home/${USER}:rw \
    -v /data_fast/IPROFI/test:/home/${USER}/YaProfi/query:ro \
    -v /data_fast/IPROFI/train:/home/${USER}/YaProfi/mapping:ro \
    -v /home/yaprofi2021/${USER}/Downloads:/home/${USER}/model \
    iprofi_${USER}:latest

