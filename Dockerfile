# Base image
#FROM ubuntu:20.04 
FROM nvidia/cudagl:11.3.0-devel-ubuntu20.04
#FROM nvidia/cudagl:10.1-devel-ubuntu16.04
# Setup basic packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    vim \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    libglfw3-dev \
    libglm-dev \
    libx11-dev \
    libomp-dev \
    libegl1-mesa-dev \
    pkg-config \
    wget \
    zip \
    net-tools \
    unzip &&\
    rm -rf /var/lib/apt/lists/*
    

# Install conda
RUN curl -L -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  &&\
    chmod +x ~/miniconda.sh &&\
    ~/miniconda.sh -b -p /opt/conda &&\
    rm ~/miniconda.sh &&\
    /opt/conda/bin/conda install numpy pyyaml scipy ipython mkl mkl-include &&\
    /opt/conda/bin/conda clean -ya
ENV PATH /opt/conda/bin:$PATH

# Install cmake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh
RUN mkdir /opt/cmake
RUN sh /cmake-3.14.0-Linux-x86_64.sh --prefix=/opt/cmake --skip-license
RUN ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake
RUN cmake --version

# Conda environment
RUN conda create -n habitat python=3.7 cmake=3.14.0

RUN git config --global user.email "2675299845@qq.com"
RUN git config --global user.name "Jackey-FEI"
RUN git clone https://github.com/Jackey-FEI/PySocialForce.git
RUN conda create -n robostackenv python=3.9 -c conda-forge
RUN /bin/bash -c ". activate robostackenv; conda config --env --add channels conda-forge; conda config --env --add channels robostack-experimental; conda config --env --add channels robostack; conda config --env --set channel_priority strict"

WORKDIR /PySocialForce
RUN pip install 'pysocialforce[test,plot]'


ENV ROS_MASTER_URI=http://172.17.0.1:11311
ENV ROS_IP=172.17.0.1
