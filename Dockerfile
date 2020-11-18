FROM debian:latest

ENV HOSTNAME darkly
ENV HOME /home/darkly

# Install dependencies
RUN apt-get update -y && apt-get install -y \
        wget \
        curl \
        dirb \
        python3.7 python3-dev \
        python3-requests \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
    && apt-get install -y python3-bs4 \
    && useradd -s /bin/bash darkly \
    && echo 'PS1="[\u@docker]\033[0;33m \w # \033[0;0m"' > /etc/bash.bashrc

USER darkly

WORKDIR /home/darkly
COPY . .
