# SSH

## 基本使用

SSH可以远程连接服务器的终端。命令格式如下，其中`<user>`为远程服务器上的用户名，`<hostname>`是远程服务器的网络地址，可以是IP地址或域名，也可以是`~/.ssh/config`文件中定义的主机。如果指定了`<command>`参数，则SSH在连接成功后会自动执行命令，将结果输出到终端并在执行结束后断开连接。

```bash
ssh <user>@<hostname> [<command>]
```

若客户端的用户名和服务器的用户名相同，可以省略`<user>`参数，如

```bash
ssh <hostname> [<command>]
```

## 端口转发

SSH提供了`-L`、`-R`、`-D`参数，分别可以实现本地端口转发、远程端口转发与动态端口转发。使用`-N`参数可以在不连接远程终端，只实现端口转发。为清晰表述各个端口，本节中假设客户端A、服务器B和另一主机C。客户端A通过SSH连接至服务器B。

### 本地端口转发

使用`-L`参数可以打开SSH的本地端口转发功能。由于`-L`参数将指向客户端本地的请求转发给服务器，因此称为本地端口转发。启动本地端口转发的命令格式如下

```bash
ssh -L [<bind-addr>]:<port-of-A>:<addr-of-C>:<port-of-C> <user>@<hostname>
```

以上命令表示将客户端A上指向`<port-of-A>`端口的本地请求通过SSH转发给服务器B，由服务器B向远程主机`<addr-of-C>`的`<port-of-C>`端口发起请求。若指定`<bind-addr>`，则SSH会监听`<bind-addr>`地址，并只转发目标为`<bind-addr>`的请求。

### 远程端口转发

使用`-R`参数可以打开SSH的远程端口转发功能。`-R`端口将指向远程服务器的请求转发给客户端，因此称为远程端口转发。启动远程端口转发的命令格式如下

```bash
ssh -R [<bind-addr>]:<port-of-B>:<addr-of-C>:<port-of-C> <user>@<hostname>
```

以上命令表示将服务器B上指向`<port-of-B>`端口的请求通过SSH转发给客户端A，由客户端A向另一台主机`<addr-of-C>`的`<port-of-C>`端口发起请求。若指定`<bind-addr>`，则SSH会监听`<bind-addr>`地址，并只转发目标为`<bind-addr>`的请求。

### 动态端口转发

动态端口转发的命令格式如下

```bash
ssh -D <port-of-A> <user>@<hostname>
```

以上命令表示将客户端A上指向`<port-of-A>`的请求通过SSH转发给服务器B，由B代为发起请求，并将访问结果传输回本地。

若要转发所有本地网络请求，设置SOCKS5代理将本地请求重定向到`<port-of-A>`即可。

## 密钥登录

SSH默认使用用户名-密码的方式进行验证，每次登录需要输入密码。可以配置SSH使用密钥对客户端进行验证，此后使用该客户端登录就不再需要输入密码。步骤如下

1. 在客户端执行`ssh-keygen`命令生成密钥对，执行完成后会在`~/.ssh`目录下生成私钥文件`id_rsa`与公钥文件`id_rsa.pub`；
2. 执行`ssh-copy-id <user>@<hostname>`命令，将公钥复制到远程主机的`~/.ssh/authorized_key`文件中（手动复制粘贴也可以）。

## 文件传输

`scp`可以借助SSH tunnel实现文件传输。命令格式如下

```bash
scp SOURCE DESTINATION
```

表示将文件SOURCE复制到DESTINATION下。SOURCE和DESTINATION可以是：

1. 本地有效路径
2. 格式为`<user>@<ip>:<path>`的远程路径