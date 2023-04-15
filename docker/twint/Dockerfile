FROM ubuntu:22.04 AS ubuntu-base

### add a non-root user
RUN apt update && apt install sudo

ARG USER_NAME=${USER_NAME} 
ARG GROUP_NAME=${USER_NAME} && UID=${UID} && GID=${GID} 
ARG PASSWD=${USER_NAME} && HOME=/home/${USER_NAME}
ENV USER_NAME=${USER_NAME} 
ENV UID=${UID} 
ENV GID=${GID}
ENV GROUP_NAME=${USER_NAME}
RUN groupadd -g ${GID} ${GROUP_NAME} && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} -G sudo ${USER_NAME} && \
    echo ${USER_NAME}:$PASSWD | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ${USER_NAME}

WORKDIR ${HOME}


FROM ubuntu-base:latest AS twint-base

### install python, pip and python
RUN sudo apt-get update && \
    sudo apt-get install -y python3.6 build-essential wget python3-setuptools git pipenv pip

### pip
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/p/python3-stdlib-extensions/python3-distutils_3.6.5-3_all.deb && \
    sudo dpkg -x python3-distutils_3.6.5-3_all.deb / 
#    unlink ./apt_pkg.cpython-36m-x86_64-linux-gnu.so && \
#    sudo ln -s /usr/lib/python3/dist-packages/apt_pkg.cpython-38-x86_64-linux-gnu.so apt_pkg.so && \
#    sudo apt install pipenv
# RUN sudo pipenv install git+https://github.com/twintproject/twint.git#egg=twint   
# RUN pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

### install twint
# RUN git clone --depth=1 https://github.com/twintproject/twint.git
# WORKDIR ${HOME}/twint
# RUN pip install . -r requirements.txt

FROM twint-base AS twint-python

ENV POETRY_VERSION=1.3.1 \
    POETRY_HOME=$HOME
ENV PATH $PATH:$HOME/.poetry/bin:$HOME/.local/bin:$HOME/bin:$PATH

# ### install python and poetry
# RUN sudo apt install --no-install-recommends -y python3.10 python3-pip python3.10-dev \
#     python3-setuptools python3-distutils curl build-essential && \
#     sudo update-alternatives --install /usr/local/bin/python python /usr/bin/python3.10 1  && \
#     sudo pip install --upgrade pip
# RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python -  && \
#     poetry config virtualenvs.create false && \
#     poetry export -f requirements.txt --output requirements.txt --without-hashes && \
#     pip3 install -r requirements.txt --user --no-deps
