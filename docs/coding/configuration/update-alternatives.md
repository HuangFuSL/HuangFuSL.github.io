# update-alternatives

`update-alternatives`是用于管理软链接的命令。

## 基础使用

### 创建链接

使用`--install`参数创建指向一个目标的软链接，命令的基本格式如下

```bash
update-alternatives --install <destination> <entry-name> <source> <priority>
```

以上命令创建一个`<entry-name>`的软链接条目，将`<source>`指向`<destination>`。当有多个`<source>`指向同一个`<destination>`时，默认`<priority>`更大的生效。

### 查询条目

使用`--display`参数查询`<entry-name>`下的命令指向：

```bash
update-alternatives --display <entry-name>
```

使用`--get-selections`参数查询所有的条目和配置状态。

```bash
update-alternatives --get-selections
```

输出格式如下

```text
arptables                      auto     /usr/sbin/arptables-nft
awk                            auto     /usr/bin/gawk
builtins.7.gz                  auto     /usr/share/man/man7/bash-builtins.7.gz
c++                            auto     /usr/bin/g++
c89                            auto     /usr/bin/c89-gcc
c99                            auto     /usr/bin/c99-gcc
cc                             auto     /usr/bin/gcc
cpp                            auto     /usr/bin/cpp
cuda                           auto     /usr/local/cuda-11.7
cuda-11                        auto     /usr/local/cuda-11.7
```

### 切换链接

使用`--config`参数可以列出并选择需要的软链接，命令的基本格式如下：

```bash
update-alternatives --config <entry-name>
```

以上命令会列出`<entry-name>`下的所有条目。

```text
There are 2 choices for the alternative gcc (providing /usr/bin/gcc).

  Selection    Path             Priority   Status
------------------------------------------------------------
* 0            /usr/bin/gcc-11   2         auto mode
  1            /usr/bin/gcc-11   2         manual mode
  2            /usr/bin/gcc-12   1         manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

或者，也可以用`--set`参数指定链接的目标，格式为：

```bash
update-alternatives --set <entry-name> <source>
```

以上命令使用`<source>`作为`<entry-name>`条目的指向。

使用`--auto`参数恢复默认的目标指向。

```bash
update-alternatives --auto <entry-name>
```

### 删除链接

使用`--remove`参数删除一个条目下的链接。

```bash
update-alternatives --remove <entry-name> <source>
```
