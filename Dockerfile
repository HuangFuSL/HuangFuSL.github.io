FROM python:bullseye

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
# Create a virtual environment, activate it and install dependencies
RUN python3 -m venv /root/venv \
    && . /root/venv/bin/activate \
    && pip3 install -r /tmp/requirements.txt --no-cache-dir

# Override the entrypoint defined in the base image
WORKDIR /