FROM ubuntu
RUN apt update \\
    && apt install git python3 python3-pip \
    && git clone https://github.com/HuangFuSL/HuangFuSL.github.io.git \
    && cd HuangFuSL.github.io \
    && pip3 install -r requirements.txt