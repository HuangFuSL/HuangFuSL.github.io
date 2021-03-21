FROM squidfunk/mkdocs-material

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root

RUN pip install pip -U \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

COPY requirements.txt .
RUN pip install -r requirements.txt

# RUN mkdir HuangFuSL.github.io
# WORKDIR /root/HuangFuSL.github.io
# ADD . .
RUN git clone https://github.com/HuangFuSL/HuangFuSL.github.io
WORKDIR /root/HuangFuSL.github.io


EXPOSE 8000

CMD git pull \
    && mkdocs serve --dev-addr=0.0.0.0:8000