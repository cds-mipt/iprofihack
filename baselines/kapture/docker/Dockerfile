#FROM ubuntu:18.04
FROM nvidia/cudagl:10.0-devel-ubuntu18.04
MAINTAINER CogModel

# Get dependencies
RUN 	apt-get update \
 	&& apt-get install -y --no-install-recommends \
    	git \
    	wget\
    	curl \
    	python3.6 python3-pip 

# make sure pip 3 is >= 20.0 to enable use-feature=2020-resolver
RUN pip3 install --upgrade pip
RUN 	python3 -m pip install --upgrade setuptools wheel twine

#RUN	pip install --upgrade ipykernel
RUN	pip install jupyter notebook
RUN	apt-get install -y vim nano

#install kapture from pip.
RUN     python3 -m pip install kapture

# install kapture-localization
RUN     python3 -m pip install "torch==1.4.0" "torchvision==0.5.0" "scikit_learn==0.20.2"
RUN 	apt-get update  \
	&& apt-get install -y \
        zip unzip


# save space: purge apt-get
RUN     rm -rf /var/lib/apt/lists/*
RUN 	apt-get update && \
      	apt-get -y install sudo

RUN	mkdir -p /home/${SOURCE_PREFIX}
WORKDIR /home/${SOURCE_PREFIX}
ENTRYPOINT jupyter notebook --ip 0.0.0.0 --port 8889 --no-browser --allow-root -y


# setup environment
ENV     LANG C.UTF-8
ENV     LC_ALL C.UTF-8
ENV     DEBIAN_FRONTEND noninteractive
USER	root
# arguments
ARG     MAKE_OPTIONS="-j8"
ARG 	USER=docker_kapture
ARG 	UID=1000
ARG 	GID=1000

ARG     SOURCE_PREFIX="${USER}/YaProfi"
ARG 	PW=user

