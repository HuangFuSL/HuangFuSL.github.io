# apt：Ubuntu 包管理工具

Ubuntu下的包管理工具是`dpkg`，有两个前端`apt`和`apt-get`。

## 安装中断后的恢复

在某个软件安装中断（如Ctrl+C或kill）后，软件的安装并没有实际完成，需要继续执行安装操作或回滚到安装之前的状态。

若要继续安装，可以执行如下命令，`dpkg`会尝试对已经解压未完成安装的软件包进行恢复。

```bash
sudo dpkg --configure -a
```

若要回滚安装，需要先在`dpkg`的安装记录下找到未完全安装的包，将其删除后重新配置`apt`。此处以`nvidia-cudnn`为例：

```bash
sudo ls -l /var/lib/dpkg/info | grep -i nvidia-cudnn
sudo mv /var/lib/dpkg/info/nvidia-cudnn.* /tmp
sudo dpkg --configure -a
sudo apt-get autoremove
```