# From TeXLive image
FROM registry.gitlab.com/islandoftex/images/texlive:TL2023-2023-08-13-full

# Reconfigure dependencies
RUN sed -i 's/testing/stable/g' /etc/apt/sources.list \
    && apt-get update \
    && apt-get remove -y \
        nodejs \
        ghostscript \
        python3 \
    && apt-get autoremove -y \
    && apt-get install -y \
        nodejs \
        ghostscript \
        python3 \
        python3-pip \
        python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /tmp/requirements.txt
# Create a virtual environment, activate it and install dependencies
RUN python3 -m venv /root/venv \
    && . /root/venv/bin/activate \
    && pip3 install -r /tmp/requirements.txt --no-cache-dir

# Override the entrypoint defined in the base image
WORKDIR /