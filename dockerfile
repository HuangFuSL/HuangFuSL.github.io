FROM squidfunk/mkdocs-material

# Install dependencies
COPY . /root/HuangFuSL.github.io
WORKDIR /root/HuangFuSL.github.io

RUN python ci/bootstrap.py

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

RUN mkdocs build -d build

EXPOSE 8000

ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
