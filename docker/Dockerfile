FROM ubuntu:bionic

# Update
RUN apt-get update
RUN apt-get upgrade -y

# Install Dockerfile Utilities
RUN apt-get install gcc wget git -y

# Install Anaconda3
RUN apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 -y
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
RUN bash Anaconda3-2020.11-Linux-x86_64.sh -b
ENV PATH="/root/anaconda3/bin:$PATH"

# Configure git
RUN git config --global user.name "Will Queree"
RUN git config --global user.email "wqueree@gmail.com"

# Clone InterFuser Repository
RUN git clone https://github.com/wqueree/InterFuser.git

# Install InterFuser
WORKDIR /InterFuser
RUN git checkout develop
RUN conda env create -f docker/environment.yml
WORKDIR /InterFuser/interfuser
RUN ls -la /root/anaconda3/envs
SHELL ["conda", "run", "-n", "interfuser", "/bin/bash", "-c"]
RUN python setup.py develop

# Install CARLA
WORKDIR /InterFuser
RUN chmod +x setup_carla.sh
RUN ./setup_carla.sh
RUN easy_install carla/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg

# Install Development Utilities
RUN apt-get install neofetch -y

# Finalise
WORKDIR /
RUN conda init bash
WORKDIR /InterFuser