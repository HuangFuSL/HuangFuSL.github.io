FROM ubuntu
RUN apt update -y \
    && apt install git python3 python3-pip -y \
    && git clone https://github.com/HuangFuSL/HuangFuSL.github.io.git \
    && cd HuangFuSL.github.io \
    && pip3 install -r requirements.txt