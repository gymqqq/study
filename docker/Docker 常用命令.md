# 03. Docker 介绍

## 1. 查看镜像

```bash
docker images
```

## 2. 搜索镜像

```bash
docker search 镜像名
```

## 3. 拉取镜像

拉取镜像就是从中央仓库下载镜像到本地。

```bash
docker pull 镜像名称:tag
```

如果不声明tag，默认拉取latest版本。

可以通过 https://hub.docker.com 搜索该镜像，查看支持的tag信息。

## 4. 删除镜像

```bash
docker rmi 镜像id | 镜像名称 | 镜像名称:tag
```

**使用镜像id删除的时候，输入id的前几位即可**

> 删除镜像的时候，必须保证没有镜像被使用，也就是说没有通过镜像创建容器，如果有，则必须先删除容器

`docker images -q` 可以查询到所有镜像的ID

```bash
#以下命令可以删除所有镜像
docker rmi docker images -q
```

## 5. 查看当前运行容器

```bash
docker ps
# 查看所有容器
docker ps -a
# 查看退出容器
docker ps -fstatus=exited
#查看最近运行容器
docker ps -l
```

## 6. 容器启动命令

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

- -i：表示运行容器；
- -t：表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端；
- --name：为创建的容器命名；
- -V：表示目录映射关系（前者是宿主机目录，后者是映射到宿主机上的目录），可以使用多个 -V 做多个目录或文件映射。注意：最好做目录映射，在宿主机上做修改，然后共享到容器上；
- -d：在run后面加上-d参数，则会创建一个守护式容器在后台运行（这样创建容器后不会自动登录容器，如果只加-i-t两个参数，创建容器后就会自动进容器里）；
- -p：表示端口映射，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p做多个端口映射。
- -P：随机使用宿主机的可用端口与容器内暴露的端口映射。

```bash
# MySQL
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql
# Redis
docker run --name redis -p 6379:6379 -d redis
```

守护进程下进入容器

```bash
sudo docker exec -it CONTAINER COMMAND [ARG...]
# MySQL
sudo docker exec -it mysql bash
```

### 自启动

```bash
sudo docker update --restart=always [CONTAINER...]
```

## 7. 停止与启动容器

```bash
# 停止容器
docker stop 镜像id | 镜像名称
# 启动容器
docker start 镜像id | 镜像名称
```

## 8.删除容器

```
docker rm 容器名称 #必须先删除容器才能删除镜像
```

## 9. 运行容器

python3.8

~~~shell
sudo docker run -it python:3.8 /bin/bash
~~~



```
docker run --name sp_backend -itd --restart=always -p 8005:8000 -v /home/ubuntu/src:/root -d registry.cn-
linux系统中的/home/ubuntu/src 映射到 dockers中的root
hangzhou.aliyuncs.com/yrz_docker_images/python:3.8 /bin/bash
```



## 11.文件拷贝

如果我们需要将文件拷贝到容器内可以使用cp命令。

```bash
docker cp 需要拷贝的文件或目录 容器名称:容器目录
```

也可以将文件从容器内拷贝出来。

```bash
docker cp 容器名称:容器目录 需要拷贝的文件或目录
```

