# Docker

`docker`是用于提供容器镜像的软件。镜像是一套配置好的运行环境，可以快速部署为应用程序。

## Docker registry

Docker registry是docker的镜像源。

### 登录

登录终端后，才能从网络上push和pull镜像。登录的命令为

```bash
docker login <registry-url>
```

如果没有指定`<registry-url>`，则默认使用Docker registry `docker.io`。

登录过程中会请求用户输入用户名和密码（或Access Token）。如果账户配置了2FA，则只能通过Access Token的方式登录。登录信息保存在`~/.docker/config.json`或系统的钥匙串中。如果加上`--password-stdin`参数，docker会从命令行中读取密码。

!!! info "配置docker使用macOS钥匙串"

    1. 执行`docker logout`，删除原先的登录凭证；
    2. 从Homebrew安装`docker-credential-helper`；
    3. 在`~/.docker/config.json`中加入如下一行：

    ```json
    {
        "credsStore": "osxkeychain"
    }
    ```

    4. 重新执行`docker login`登录；
    5. 确认`~/.docker/config.json`里没有登录凭证：

    ```json
    {
        "auths": {
                "https://index.docker.io/v1/": {}
        }
    }
    ```

### 第三方镜像源列表

!!! note "ghcr.io"

    `ghcr.io`是GitHub提供的镜像源，可以无缝集成至GitHub Actions。

    验证方式：

    1. 使用GitHub Access Token验证，Access Token必须至少具备`read:packages`权限，如果要推送镜像，则还需要`write:packages`权限
    2. 在GitHub Actions中可以使用`GITHUB_TOKEN`验证。

## Dockerfile

`dockerfile`文件用来将一套环境打包成镜像。每一条指令都对应了容器镜像的一层。

### Docker镜像基础

Docker镜像的基本格式为`[<registry-name>]/<namespace>/<image-name>:[<tag>]`

* `<registry-name>`：可选，决定Docker镜像发布在哪个Registry上；
* `<namespace>`：一般是用户名；
* `<image-name>`：镜像名称；
* `<tag>`：可选，镜像版本，默认为`latest`

使用`docker pull`命令从registry下载镜像。

执行`docker build <path>`来从Dockerfile构建镜像。用`-t`参数可以指定镜像的名称和版本。

在镜像构建完成后，执行`docker push <image-name>`将镜像推送到对应的registry上。

### `ADD`

`ADD`（或`COPY`）命令将本地或互联网上的文件复制到容器镜像中。

```dockerfile
ADD <local-path> <image-path>
```

* 如果路径中包含空格，需要用双引号把路径括起来；
* `<local-path>`支持通配符`*?`；

### `FROM`

`FROM`命令指明当前的`dockerfile`是在哪一个镜像上执行的。每个Dockerfile必须有一条`FROM`语句。

!!! note "空白Docker镜像"

    `scratch`是一个预定义的空白Docker镜像，也是所有Docker镜像的起始。

    ```
    FROM scratch
    ```

### `RUN`

`RUN`执行一个命令，如果要执行多个命令可以用`&&`连接

```dockerfile
RUN command-1 && \
    command-2 && \
    ...
```

## 配置TLS远程访问

Docker是c/s架构，意味着可以从远程访问主机的Docker daemon，从远程直接操作Docker环境，容器和镜像均保存在远程主机上。但在网络上需要TLS加密传输以保证安全，因此需要先配置好openssl，并且有一个解析到服务器的域名，如`www.example.com`。

### 服务器配置

`dockerd`是Docker daemon的可执行程序。

=== "Docker Daemon"

    在服务器端，需要执行如下命令。

    1. 生成CA密钥

        ```bash
        openssl genrsa -aes256 -out ca-key.pem 4096
        openssl req -new -x509 -days 365 -key ca-key.pem -sha256 -out ca.pem # (1)
        ```

        1. 会请求输入一些信息，其中`Common Name`一条需要填写服务器对应的域名。

    2. 生成服务器密钥和证书

        ```bash
        openssl genrsa -out server-key.pem 4096
        openssl req -subj "/CN=www.example.com" -sha256 -new -key server-key.pem -out server.csr
        echo subjectAltName = DNS:$HOST,IP:8.8.8.8 >> extfile.cnf # (1)
        echo extendedKeyUsage = serverAuth >> extfile.cnf
        openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.pem -CAkey ca-key.pem \
            -CAcreateserial -out server-cert.pem -extfile extfile.cnf
        ```

        1. 如果不需要IP地址访问，可以删除相关条目。

    3. 生成客户端密钥和证书

        ```bash
        openssl genrsa -out key.pem 4096
        openssl req -subj '/CN=client' -new -key key.pem -out client.csr
        echo extendedKeyUsage = clientAuth > extfile-client.cnf
        openssl x509 -req -days 365 -sha256 -in client.csr -CA ca.pem -CAkey ca-key.pem \
            -CAcreateserial -out cert.pem -extfile extfile-client.cnf
        ```

    4. 清理其余文件，只留下`.pem`证书文件，并且调整证书文件的权限

        ```bash
        rm -v client.csr server.csr extfile.cnf extfile-client.cnf
        chmod -v 0400 ca-key.pem key.pem server-key.pem
        chmod -v 0444 ca.pem server-cert.pem cert.pem
        ```

    5. 启动Docker daemon

        ```bash
        dockerd \
            --tlsverify \
            --tlscacert=ca.pem \
            --tlscert=server-cert.pem \
            --tlskey=server-key.pem \
            -H=0.0.0.0:2376
        ```

    6. 分发客户端证书`ca.pem`、`cert.pem`、`key.pem`。客户端可以通过以下命令连接

        ```bash
        docker --tlsverify \
            --tlscacert=ca.pem \
            --tlscert=cert.pem \
            --tlskey=key.pem \
            -H=$HOST:2376
        ```

=== "Docker Desktop"

    在Windows中，Docker通过WSL或者Hyper-V虚拟化实现Linux环境。因此，如果在Windows下直接执行`dockerd.exe`，得到的是运行Windows容器的Docker。如果要远程连接运行Linux的Docker环境，需要使用`docker-remote-api-tls`。

    !!! danger "Docker Desktop Engine 配置文件"

        在Docker Desktop里的Settings - Engine里修改TLS参数配置，会导致Docker Engine无法启动。

    1. 执行`git clone https://github.com/kekru/docker-remote-api-tls.git`克隆镜像
    2. 编辑`docker-compose.yml`，替换`<password>`、`<domain-or-ip>`、`<client-cert-path>`中的内容

        ```yaml
        version: "3.4"
        services:
            remote-api:
                image: kekru/docker-remote-api-tls:v0.4.0
                ports:
                    - 2376:443
                environment:
                    - CREATE_CERTS_WITH_PW=<password>
                    - CERT_HOSTNAME=<domain-or-ip>
                volumes:
                    - <client-cert-path>:/data/certs # (1)
                    - /var/run/docker.sock:/var/run/docker.sock:ro
        ```

        1. 不加这一行也行，可以直接从Docker Desktop里复制

    3. 执行`docker-compose up -d`运行容器，注意在远程连接过程中需要保证容器始终开启

### 客户端配置

1. 将`ca.pem`、`cert.pem`、`key.pem`复制到客户端的`~/.docker`目录下
2. 设置环境变量（只适用于从终端访问Docker的情况）

    ```bash
    export $DOCKER_TLS_VERIFY=1
    export $DOCKER_HOST="tcp://<domain-or-ip>:2376"
    ```

3. 或者，可以创建一个Docker context

    ```bash
    docker context create remote --docker \
        "host=tcp://<domain-or-ip>:2376,ca=~/.docker/ca.pem,cert=~/.docker/cert.pem,key=~/.docker/key.pem
    ```

4. 此后，Docker会默认使用远程连接。

如果连接成功，执行`docker version`会同时输出客户端和服务器两者的版本信息，如

```text
Client: Docker Engine - Community
 Version:           24.0.5
 API version:       1.43
 Go version:        go1.20.6
 Git commit:        ced0996600
 Built:             Wed Jul 19 19:44:22 2023
 OS/Arch:           darwin/arm64
 Context:           default

Server: Docker Desktop 4.21.1 (114176)
 Engine:
  Version:          24.0.2
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.4
  Git commit:       659604f
  Built:            Thu May 25 21:52:17 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.21
  GitCommit:        3dce8eb055cbb6872793272b4f20ed16117344f8
 runc:
  Version:          1.1.7
  GitCommit:        v1.1.7-0-g860f061
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

!!! warning "挂载卷"

    在Docker中，无论是使用`-v`参数还是`--mount`参数挂载的卷的源路径都是相对于Docker Daemon而言的。

### 参考阅读

Docker registry：

* [Working with the Container registry (GitHub)](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

Dockerfile：

* [Dockerfile reference](https://docs.docker.com/engine/reference/builder)

远程访问Docker daemon：

* [Windows Docker 主机远程管理](https://learn.microsoft.com/zh-cn/virtualization/windowscontainers/management/manage_remotehost)
* [Protect the Docker daemon socket](https://docs.docker.com/engine/security/protect-access/)
* [dockerd](https://docs.docker.com/engine/reference/commandline/dockerd/)
* [Docker Remote API with TLS client authentication via container](https://github.com/kekru/docker-remote-api-tls)
* [How can I mount a volume of files to a remote docker daemon?](https://stackoverflow.com/questions/51305537/how-can-i-mount-a-volume-of-files-to-a-remote-docker-daemon)