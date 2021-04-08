FROM squidfunk/mkdocs-material

# Install dependencies
WORKDIR /root

COPY requirements.txt .
RUN apk add --no-cache --virtual \
    .build \
    gcc g++ libgcc musl-dev \
    jpeg-dev zlib-dev make libffi-dev libtool zeromq-dev \
    && pip install --no-input --no-cache-dir -r requirements.txt \
    && apk del \
    .build \
    gcc g++ libgcc musl-dev \
    jpeg-dev zlib-dev make libffi-dev libtool zeromq-dev

RUN apk add --no-cache libzmq libjpeg nodejs

RUN git clone https://github.com/HuangFuSL/HuangFuSL.github.io --depth=1
WORKDIR /root/HuangFuSL.github.io


EXPOSE 8000

ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
