FROM ubuntu:bionic

# User Details
ENV USER="wlq20"
ENV NAME="Will Queree"
ENV EMAIL="wqueree@gmail.com"

# Create User
RUN adduser ${USER}
RUN adduser ${USER} sudo

# Update
RUN apt-get update
RUN apt-get upgrade -y

# Install Dockerfile Utilities
RUN apt-get install gcc wget git -y

# Install Anaconda3
RUN apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 -y
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
RUN chmod +x ./Anaconda3-2020.11-Linux-x86_64.sh
USER ${USER}
RUN ./Anaconda3-2020.11-Linux-x86_64.sh -b
ENV PATH="/${USER}/anaconda3/bin:$PATH"
USER root

# Configure git
RUN git config --global user.name ${NAME}
RUN git config --global user.email ${EMAIL}
# Clone InterFuser Repository
RUN git clone https://github.com/wqueree/InterFuser.git

# Install InterFuser
USER ${USER}
WORKDIR /InterFuser
RUN git pull
RUN git checkout develop
RUN conda env create -f docker/environment.yml
WORKDIR /InterFuser/interfuser
SHELL ["conda", "run", "-n", "interfuser", "/bin/bash", "-c"]
RUN python setup.py develop

# Install CARLA
WORKDIR /InterFuser
RUN chmod +x setup_carla.sh
RUN ./setup_carla.sh
RUN easy_install carla/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg

# Install Development Utilities
USER root
RUN apt-get install neofetch -y
USER ${USER}

# Finalise
WORKDIR /
RUN conda init bash
