# 1.常见的处理目录的命令

几个常见的处理目录的命令吧：

- ls（英文全拼：list files）: 列出目录及文件名
- cd（英文全拼：change directory）：切换目录
- pwd（英文全拼：print work directory）：显示目前的目录
- mkdir（英文全拼：make directory）：创建一个新的目录
- rmdir（英文全拼：remove directory）：删除一个空的目录
- cp（英文全拼：copy file）: 复制文件或目录
- rm（英文全拼：remove）: 删除文件或目录
- mv（英文全拼：move file）: 移动文件与目录，或修改文件与目录的名称

你可以使用 *man [命令]* 来查看各个命令的使用文档，如 ：man cp。

## 1.1 list files(ls)

~~~shell
ls -[ 选项与参数] 目录
~~~

- -a ：全部的文件，连同隐藏文件( 开头为 . 的文件) 一起列出来(常用)
- -d ：仅列出目录**本身**，而不是列出目录内的文件数据(常用)
- -l ：长数据串列出，包含文件的属性与权限等等数据；(常用)

~~~shell
ls -a
~~~

![image-20240724162610330](.\Linux_Com_images\ls_a.png)

~~~shell
ls -d
~~~



![image-20240724162634787](.\Linux_Com_images\image-20240724162634787.png)

~~~shell
ls -l
~~~

![image-20240724162802088](.\Linux_Com_images\image-20240724162802088.png)

## 1.2 cd(Change Directory)

切换目录命令，即可以加相对路径，也可以加绝对路径。

```shell
cd [相对路径或绝对路径]
```

## 1.3 pwd( Print Working Directory )

显示当前目录

~~~shell
pwd [-P]
~~~

[-P]  显示出确实的路径，(如，软链接，直接显示链接路径)

## 1.4 mkdir (make directory)

创建新目录命令

```shell
mkdir [-mp] 目录名称
```

- -m (mode)：配置文件的权限！直接配置，不需要看默认权限 (umask) 的脸色～
- -p ：帮助你直接将所需要的目录(包含上一级目录)递归创建起来！(强行创建目录)

![image-20240724164109146](.\Linux_Com_images\image-20240724164109146.png)

![image-20240724164153795](.\Linux_Com_images\image-20240724164153795.png)

## 1.5 rmdir (remove directory)

删除空的目录

```shell
rmdir [-p] 目录名称
```

- **-p ：**从该目录起，一次删除多级空目录

![image-20240724164508902](.\Linux_Com_images\image-20240724164508902.png)

删除一个空目录时，只需要rmdir即可。
若空目录下仍有目录，则需要递归删除，通过增加[-p]属性即可。

## 1.6 cp(copy)

```shell
cp [-adfilprsu] 来源档(source) 目标档(destination)
cp [options] source1 source2 source3 .... directory
cp [ ]  A B 
把A通过[ ]的方式粘贴到B里
```

- **-a：**相当于 -pdr 的意思，至于 pdr 请参考下列说明；(常用)
- **-d：**若来源档为链接档的属性(link file)，则复制链接档属性而非文件本身；
- **-f：**为强制(force)的意思，若目标文件已经存在且无法开启，则移除后再尝试一次；
- **-i：**若目标档(destination)已经存在时，在覆盖时会先询问动作的进行(常用)
- **-l：**进行硬式链接(hard link)的链接档创建，而非复制文件本身；
- **-p：**连同文件的属性一起复制过去，而非使用默认属性(备份常用)；
- **-r：**递归持续复制，用于目录的复制行为；(常用)
- **-s：**复制成为符号链接档 (symbolic link)，亦即『捷径』文件；
- **-u：**若 destination 比 source 旧才升级 destination ！

![image-20240724165136857](.\Linux_Com_images\image-20240724165136857.png)

## 1.7 rm(remove)

移除文件或目录

```shell
 rm [-fir] 文件或目录
```

- -f ：就是 force 的意思，忽略不存在的文件，不会出现警告信息；

  ​       文件不存在该属性也可以使用，强制删除。

- -i ：互动模式，在删除前会询问使用者是否动作

- -r ：递归删除啊！最常用在目录的删除了！这是非常危险的选项！！！

  ​       直接删除目录，目录下面还有目录也会被删除。

![image-20240724165420330](.\Linux_Com_images\image-20240724165420330.png)

![image-20240724165841307](.\Linux_Com_images\image-20240724165841307.png)

## 1.8 mv(move)

移动文件与目录，或修改名称

```shell
mv [-fiu] source destination
mv [ ] A B #把A移到B
mv [options] source1 source2 source3 .... directory
mv [ ] A B C D #把A B C 都移到 D里
```

- -f ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；
- -i ：若目标文件 (destination) 已经存在时，就会询问是否覆盖！
- -u ：若目标文件已经存在，且 source 比较新，才会升级 (update)

# 2.Linux 文件内容查看

- cat 由第一行开始显示文件内容
- tac 从最后一行开始显示，可以看出 tac 是 cat 的倒着写！
- nl  显示的时候，顺道输出行号！
- more 一页一页的显示文件内容
- less 与 more 类似，但是比 more 更好的是，他可以往前翻页！
- head 只看头几行
- tail 只看尾巴几行

## 2.1 cat 第一行开始显示

```shell
cat [-AbEnTv]
```

- ---：直接显示内容，行号，$，tab都不显示。
- -A ：相当于 -vET 的整合选项，可列出一些特殊字符而不是空白而已；
- -n ：列出行号，连同空白行也会有行号，与 -b 的选项不同；
- -b ：列出行号，仅针对非空白行做行号显示，空白行不标行号！
- -E ：将结尾的断行字节 $ 显示出来；
- -T ：将 [tab] 按键以 ^I 显示出来；
- -v ：列出一些看不出来的特殊字符

![image-20240724170908520](.\Linux_Com_images\image-20240724170908520.png)

## 2.2 tac 从最后一行开始显示

~~~shell
tac 文件
~~~

![image-20240724171209402](.\Linux_Com_images\image-20240724171209402.png)

注：该命令无属性或参数。

## 2.3 nl 显示行号

```shell
nl [-bnw] 文件
```

- -b ：指定行号指定的方式，主要有两种：
  -b a ：表示不论是否为空行，也同样列出行号(类似 cat -n)；
  -b t ：如果有空行，空的那一行不要列出行号(默认值); 类似 cat -b
- -n ：列出行号表示的方法，主要有三种：
  -n ln ：行号在荧幕的最左方显示；
  -n rn ：行号在自己栏位的最右方显示，且不加 0 ；
  -n rz ：行号在自己栏位的最右方显示，且加 0 ；
- -w ：行号栏位的占用的位数。

![image-20240724171458336](.\Linux_Com_images\image-20240724171458336.png)

## 2.4 more 一页一页翻动

~~~shell
more 文件名
#一次显示电脑屏幕的一页
~~~

在 more 这个程序的运行过程中，几个按键可以按：

- 空白键 (space)：代表向下翻一页；
- Enter ：代表向下翻『一行』；
- /字串：代表在这个显示的内容当中，向下搜寻『字串』这个关键字；
- :f ：立刻显示出档名以及目前显示的行数；
- q ：代表立刻离开 more ，不再显示该文件内容。
- b 或 [ctrl]-b ：代表往回翻页，不过这动作只对文件有用，对管线无用。

![image-20240724171739428](.\Linux_Com_images\image-20240724171739428.png)

## 2.5 less 一页一页翻动

~~~shell
less 文件名
~~~



less运行时可以输入的命令有：

- 空格键  ：向下翻动一页；
- [pagedown]：向下翻动一行；
- [pageup] ：向上翻动一行；
- /字串   ：向下搜寻『字串』的功能；
- ?字串   ：向上搜寻『字串』的功能；
- n ：重复前一个搜寻 (与 / 或 ? 有关！)
- N：反向的重复前一个搜寻 (与 / 或 ? 有关！)
- q ：离开 less 这个程序；

![image-20240724172204063](.\Linux_Com_images\image-20240724172204063.png)

## 2.6 head 取出文件前面几行

```shell
head [-n number] 文件 
```

- -n ：后面接数字，代表显示几行的意思
  默认的情况中，显示前面 10 行

![image-20240724192927640](.\Linux_Com_images\image-20240724192927640.png)

## 2.7 tail 取出文件后面几行

```shell
tail [-n number] 文件 
```

- -n ：后面接数字，代表显示几行的意思
- -f ：表示持续侦测后面所接的档名，要等到按下[ctrl]-c才会结束tail的侦测
  默认的情况中，显示最后的十行

# 3.Linux 用户和用户组管理

Linux系统是一个多用户多任务的分时操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。
用户的账号一方面可以帮助系统管理员对使用系统的用户进行跟踪，并控制他们对系统资源的访问；
另一方面也可以帮助用户组织文件，并为用户提供安全性保护。
每个用户账号都拥有一个唯一的用户名和各自的口令。用户在登录时键入正确的用户名和口令后，就能够进入系统和自己的主目录。

实现用户账号的管理，要完成的工作主要有如下几个方面：

- 用户账号的添加、删除与修改。
- 用户口令的管理。
- 用户组的管理。

## 3.1 Linux系统用户账号的管理

用户账号的管理工作主要涉及到用户账号的添加、修改和删除。
添加用户账号就是在系统中创建一个新账号，然后为新账号分配用户号、用户组、主目录和登录Shell等资源。
刚添加的账号是被锁定的，无法使用。

### 3.1.1 useradd添加新的用户账号

```shell
useradd 选项 用户名
```

- 选项:
  - -c comment 指定一段注释性描述。
  - -d 目录 指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。
  - -g 用户组 指定用户所属的用户组。
  - -G 用户组，用户组 指定用户所属的附加组。
  - -s Shell文件 指定用户的登录Shell。
  - -u 用户号 指定用户的用户号，如果同时有-o选项，则可以重复使用其他用户的标识号。

- 用户名:

  指定新账号的登录名。![image-20240724194229316](.\Linux_Com_images\image-20240724194229316.png)

> [!CAUTION]
>
> 普通用户无法添加新用户，需要在命令前面加sudo

![image-20240724194624593](.\Linux_Com_images\image-20240724194624593.png)

此命令新建了一个用户gem，该用户的登录Shell是 `/bin/sh`，它属于group用户组，同时又属于adm和root用户组，其中group用户组是其主组。

这里可能新建组：`#groupadd group及groupadd adm`

增加用户账号就是在/etc/passwd文件中为新用户增加一条记录，同时更新其他系统文件如/etc/shadow, /etc/group等。



### 3.1.2 userdel 删除帐号

```shell
userdel 选项 用户名
```

常用的选项是 **-r**，它的作用是把用户的主目录一起删除。
-f：强制删除用户，即使用户当前已登录。

![image-20240724194917486](.\Linux_Com_images\image-20240724194917486.png)

### 3.1.3 usermod修改账号

```shell
usermod 选项 用户名
```

- 选项:
  - -c comment 指定一段注释性描述。
  - -d 目录 指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。
  - -g 用户组 指定用户所属的用户组。
  - -G 用户组，用户组 指定用户所属的附加组。
  - -s Shell文件 指定用户的登录Shell。
  - -u 用户号 指定用户的用户号，如果同时有-o选项，则可以重复使用其他用户的标识号。
  - -l 新用户名

```shell
# usermod -s /bin/ksh -d /home/z –g developer sam
```

此命令将用户sam的登录Shell修改为ksh，主目录改为/home/z，用户组改为developer。

### 3.1.4 passwd管理用户口令

```shell
passwd 选项 用户名
```

用户管理的一项重要内容是用户口令的管理。
用户账号刚创建时没有口令，但是被系统锁定，无法使用，必须为其指定口令后才可以使用，即使是指定空口令。
指定和修改用户口令的Shell命令是`passwd`。
超级用户可以为自己和其他用户指定口令，普通用户只能用它修改自己的口令。

```shell
passwd -d sam
#此命令将用户 sam 的口令删除，这样用户 sam 下一次登录时，系统就不再允许该用户登录了。
```

```shell
passwd -l sam
#passwd 命令还可以用 -l(lock) 选项锁定某一用户，使其不能登录。
```



## 3.2 Linux系统用户组的管理

### 3.2.1 groupadd增加一个新的用户组

```shell
groupadd 选项 用户组
```

可以使用的选项有：

- -g GID 指定新用户组的组标识号（GID）。
- -o 一般与-g选项同时使用，表示新用户组的GID可以与系统已有用户组的GID相同。

### 3.2.2 groupdel删除一个已有的用户组

```shell
groupdel 用户组
```

```shell
# groupdel group1
此命令从系统中删除组group1。
```

### 3.2.3 groupmod修改用户组的属性

```shell
groupmod 选项 用户组
```

常用的选项有：

- -g GID 为用户组指定新的组标识号。
- -o 与-g选项同时使用，用户组的新GID可以与系统已有用户组的GID相同。
- -n新用户组 将用户组的名字改为新名字

```shell
# groupmod –g 10000 -n group3 group2
此命令将组group2的标识号改为10000，组名修改为group3。
```

### 3.2.4 newgrp 在用户组之间切换

```shell
$ newgrp root
```

这条命令将当前用户切换到root用户组，前提条件是root用户组确实是该用户的主组或附加组。类似于用户账号的管理，用户组的管理也可以通过集成的系统管理工具来完成。

## 3.3 与用户账号有关的系统文件

### 3.3.1 /etc/passwd文件 最重要的一个文件

```shell
＃ cat /etc/passwd

root:x:0:0:Superuser:/:
daemon:x:1:1:System daemons:/etc:
bin:x:2:2:Owner of system commands:/bin:
sys:x:3:3:Owner of system files:/usr/sys:
adm:x:4:4:System accounting:/usr/adm:
uucp:x:5:5:UUCP administrator:/usr/lib/uucp:
auth:x:7:21:Authentication administrator:/tcb/files/auth:
cron:x:9:16:Cron daemon:/usr/spool/cron:
listen:x:37:4:Network daemon:/usr/net/nls:
lp:x:71:18:Printer administrator:/usr/spool/lp:
sam:x:200:50:Sam san:/home/sam:/bin/sh
#从上面的例子我们可以看到，/etc/passwd中一行记录对应着一个用户
#用户名:口令:用户标识号:组标识号:注释性描述:主目录:登录Shell

#口令：虽然这个字段存放的只是用户口令的加密串，不是明文，但是由于/etc/passwd文件对所有用户都可读，所以这仍是一个安全隐患。因此，现在许多Linux 系统（如SVR4）都使用了shadow技术，把真正的加密后的用户口令字存放到/etc/shadow文件中，而在/etc/passwd文件的口令字段中只存放一个特殊的字符，例如“x”或者“*”。

#用户标识号：通常用户标识号的取值范围是0～65535。0是超级用户root的标识号，1～99由系统保留，作为管理账号，普通用户的标识号从100开始。在Linux系统中，这个界限是500。

#登录Shell：Shell是用户与Linux系统之间的接口。Linux的Shell有许多种，每种都有不同的特点。常用的有sh(Bourne Shell), csh(C Shell), ksh(Korn Shell), tcsh(TENEX/TOPS-20 type C Shell), bash(Bourne Again Shell)等。系统管理员可以根据系统情况和用户习惯为用户指定某个Shell。如果不指定Shell，那么系统使用sh为默认的登录Shell，即这个字段的值为/bin/sh。用户的登录Shell也可以指定为某个特定的程序（此程序不是一个命令解释器）。用这一特点，我们可以限制用户只能运行指定的应用程序，在该应用程序运行结束后，用户就自动退出了系统。有些Linux 系统要求只有那些在系统中登记了的程序才能出现在这个字段中。
```

系统中有一类用户称为伪用户（pseudo users）。

这些用户在/etc/passwd文件中也占有一条记录，但是不能登录，因为它们的登录Shell为空。它们的存在主要是方便系统管理，满足相应的系统进程对文件属主的要求。

常见的伪用户如下所示：

```伪代码
伪 用 户 含 义 
bin 拥有可执行的用户命令文件 
sys 拥有系统文件 
adm 拥有帐户文件 
uucp UUCP使用 
lp lp或lpd子系统使用 
nobody NFS使用
```

### 3.3.2/etc/shadow

```shell
# 登录名:加密口令:最后一次修改时间:最小时间间隔:最大时间间隔:警告时间:不活动时间:失效时间:标志
#"登录名"是与/etc/passwd文件中的登录名相一致的用户账号
#"口令"字段存放的是加密后的用户口令字，长度为13个字符。如果为空，则对应用户没有口令，登录时不需要口令；如果含有不属于集合 { ./0-9A-Za-z }中的字符，则对应的用户不能登录。
#"最后一次修改时间"表示的是从某个时刻起，到用户最后一次修改口令时的天数。时间起点对不同的系统可能不一样。例如在SCO Linux 中，这个时间起点是1970年1月1日。
#"最小时间间隔"指的是两次修改口令之间所需的最小天数。
#"最大时间间隔"指的是口令保持有效的最大天数。
#"警告时间"字段表示的是从系统开始警告用户到用户密码正式失效之间的天数。
#"不活动时间"表示的是用户没有登录活动但账号仍能保持有效的最大天数。
#"失效时间"字段给出的是一个绝对的天数，如果使用了这个字段，那么就给出相应账号的生存期。期满后，该账号就不再是一个合法的账号，也就不能再用来登录了。
```

### 3.3.3 /etc/group

```shell
组名:口令:组标识号:组内用户列表
```

1. "组名"是用户组的名称，由字母或数字构成。与/etc/passwd中的登录名一样，组名不应重复。
2. "口令"字段存放的是用户组加密后的口令字。一般Linux 系统的用户组都没有口令，即这个字段一般为空，或者是*。
3. "组标识号"与用户标识号类似，也是一个整数，被系统内部用来标识组。
4. "组内用户列表"是属于这个组的所有用户的列表，不同用户之间用逗号(,)分隔。这个用户组可能是用户的主组，也可能是附加组。

## 3.4 添加批量用户

### （1）先编辑一个文本用户文件。

每一列按照`/etc/passwd`密码文件的格式书写，要注意每个用户的用户名、UID、宿主目录都不可以相同，其中密码栏可以留做空白或输入x号。一个范例文件user.txt内容如下：

```txt
user001::600:100:user:/home/user001:/bin/bash
user002::601:100:user:/home/user002:/bin/bash
user003::602:100:user:/home/user003:/bin/bash
user004::603:100:user:/home/user004:/bin/bash
user005::604:100:user:/home/user005:/bin/bash
user006::605:100:user:/home/user006:/bin/bash
```

### （2）以root身份执行命令 `/usr/sbin/newusers`，从刚创建的用户文件`user.txt`中导入数据，创建用户：

```
# newusers < user.txt
```

然后可以执行命令 `vipw` 或 `vi /etc/passwd` 检查 `/etc/passwd` 文件是否已经出现这些用户的数据，并且用户的宿主目录是否已经创建。

### （3）执行命令/usr/sbin/pwunconv。

将 `/etc/shadow` 产生的 `shadow` 密码解码，然后回写到 `/etc/passwd` 中，并将`/etc/shadow`的`shadow`密码栏删掉。这是为了方便下一步的密码转换工作，即先取消 `shadow password` 功能。

```
# pwunconv
```

### （4）编辑每个用户的密码对照文件。

格式为：

```
用户名:密码
```

实例文件 `passwd.txt` 内容如下：

```
user001:123456
user002:123456
user003:123456
user004:123456
user005:123456
user006:123456
```

### （5）以 root 身份执行命令 `/usr/sbin/chpasswd`。

创建用户密码，`chpasswd` 会将经过 `/usr/bin/passwd` 命令编码过的密码写入 `/etc/passwd` 的密码栏。

```
# chpasswd < passwd.txt
```

### （6）确定密码经编码写入/etc/passwd的密码栏后。

执行命令 `/usr/sbin/pwconv` 将密码编码为 `shadow password`，并将结果写入 `/etc/shadow`。

```
# pwconv
```

这样就完成了大量用户的创建了，之后您可以到/home下检查这些用户宿主目录的权限设置是否都正确，并登录验证用户密码是否正确。

# 4. Linux 磁盘管理

## 4.1 df(disk free )

列出文件系统的整体磁盘使用量

```shell
df [-ahikHTm] [目录或文件名]
```

选项与参数：

- `-h`：以人类可读的方式显示输出结果（例如，使用 KB、MB、GB 等单位）。
- `-T`：显示文件系统的类型。
- `-t <文件系统类型>`：只显示指定类型的文件系统。
- `-i`：显示 inode 使用情况。
- `-H`：该参数是 `-h` 的变体，但是使用 1000 字节作为基本单位而不是 1024 字节。这意味着它会以 SI（国际单位制）单位（例如 MB、GB）而不是二进制单位（例如 MiB、GiB）来显示磁盘使用情况。
- `-k`：这个选项会以 KB 作为单位显示磁盘空间使用情况。
- `-a`：该参数将显示所有的文件系统，包括虚拟文件系统，例如 `proc`、`sysfs` 等。如果没有使用该选项，默认情况下，`df` 命令不会显示虚拟文件系统。

~~~shell
df  #将系统内所有的文件系统列出来！
df -h  #将容量结果以易读的容量格式显示出来
df -aT  #将系统内的所有特殊文件格式及名称都列出来
df -h /etc  #将 /etc 底下的可用的磁盘容量以易读的容量格式显示
~~~

## 4.2 du(disk used)

检查磁盘空间使用量

```shell
du [-ahskm] 文件或目录名称
```

选项与参数：

- -a ：列出所有的文件与目录容量，因为默认仅统计目录底下的文件量而已。
- -h ：以人们较易读的容量格式 (G/M) 显示；
- -s ：仅显示指定目录或文件的总大小，而不显示其子目录的大小。
- -S ：包括子目录下的总计，与 -s 有点差别。
- -k ：以 KBytes 列出容量显示；
- -m ：以 MBytes 列出容量显示；

~~~shell
du #只列出当前目录下的所有文件夹容量（包括隐藏文件夹）:
du -a #将文件的容量也列出来
du -sm /* #检查根目录底下每个目录所占用的容量
# 通配符 * 来代表每个目录。
~~~

> [!CAUTION]
>
> 与 df 不一样的是，du 这个命令其实会直接到文件系统内去搜寻所有的文件数据。



## 4.3 fdisk

用于磁盘分区

```shell
fdisk [-l] 装置名称
```

选项与参数：

- -l ：输出后面接的装置所有的分区内容。若仅有 fdisk -l 时， 则系统将会把整个系统内能够搜寻到的装置的分区均列出来。

## 4.4 mkfs (make filesystem)

```shell
mkfs [-t 文件系统格式] 装置文件名
mkfs -t ext3 /dev/hdc6
将分区 /dev/hdc6 格式化为 ext3 文件系统：
```

选项与参数：

- -t ：可以接文件系统格式，例如 ext3, ext2, vfat 等(系统有支持才会生效)

查看 mkfs 支持的文件格式: mkfs[ tab] [ tab]

![image-20240725093102367](.\Linux_Com_images\image-20240725093102367.png)

## 4.5 fsck(file system check)

```shell
fsck [-t 文件系统] [-ACay] 装置名称
```

选项与参数：

- -t : 给定档案系统的型式，若在 /etc/fstab 中已有定义或 kernel 本身已支援的则不需加上此参数
- -s : 依序一个一个地执行 fsck 的指令来检查
- -A : 对/etc/fstab 中所有列出来的 分区（partition）做检查
- -C : 显示完整的检查进度
- -d : 打印出 e2fsck 的 debug 结果
- -p : 同时有 -A 条件时，同时有多个 fsck 的检查一起执行
- -R : 同时有 -A 条件时，省略 / 不检查
- -V : 详细显示模式
- -a : 如果检查有错则自动修复
- -r : 如果检查有错则由使用者回答是否修复
- -y : 选项指定检测每个文件是自动输入yes，在不确定那些是不正常的时候，可以执行 # fsck -y 全部检查修复。

查看系统有多少文件系统支持的 fsck 命令：

![image-20240725093424910](.\Linux_Com_images\image-20240725093424910.png)

## 4.6 mount/unmount

```shell
mount [-t 文件系统] [-L Label名] [-o 额外选项] [-n]  装置文件名  挂载点
```

```shell
umount [-fn] 装置文件名或挂载点
```

选项与参数：

- -f ：强制卸除！可用在类似网络文件系统 (NFS) 无法读取到的情况下；
- -n ：不升级 /etc/mtab 情况下卸除。

# 5. vi/vim

## 5.1 vi.vim的使用

基本上 vi/vim 共分为三种模式，命令模式（Command Mode）、输入模式（Insert Mode）和命令行模式（Command-Line Mode）。

![img](https://www.runoob.com/wp-content/uploads/2015/10/vi-vim-cheat-sheet-sch.gif)

### 5.1.1 命令模式

用户刚刚启动 vi/vim，便进入了命令模式。

此状态下敲击键盘动作会被 Vim 识别为命令，而非输入字符，比如我们此时按下 **i**，并不会输入一个字符，**i** 被当作了一个命令。

以下是普通模式常用的几个命令：

- **i** -- 切换到输入模式，在光标当前位置开始输入文本。
- **x** -- 删除当前光标所在处的字符。
- **:** -- 切换到底线命令模式，以在最底一行输入命令。
- **a** -- 进入插入模式，在光标下一个位置开始输入文本。
- **o**：在当前行的下方插入一个新行，并进入插入模式。
- **O** -- 在当前行的上方插入一个新行，并进入插入模式。
- **dd** -- 剪切当前行。
- **yy** -- 复制当前行。
- **p**（小写） -- 粘贴剪贴板内容到光标下方。
- **P**（大写）-- 粘贴剪贴板内容到光标上方。
- **u** -- 撤销上一次操作。
- **Ctrl + r** -- 重做上一次撤销的操作。
- **:w** -- 保存文件。
- **:q** -- 退出 Vim 编辑器。
- **:q!** -- 强制退出Vim 编辑器，不保存修改。

若想要编辑文本，只需要启动 Vim，进入了命令模式，按下 **i** 切换到输入模式即可。

命令模式只有一些最基本的命令，因此仍要依靠**底线命令行模式**输入更多命令。

### 5.1.2 输入模式

在命令模式下按下 **i** 就进入了输入模式，使用 **Esc** 键可以返回到普通模式。

在输入模式中，可以使用以下按键：

- **字符按键以及Shift组合**，输入字符
- **ENTER**，回车键，换行
- **BACK SPACE**，退格键，删除光标前一个字符
- **DEL**，删除键，删除光标后一个字符
- **方向键**，在文本中移动光标
- **HOME**/**END**，移动光标到行首/行尾
- **Page Up**/**Page Down**，上/下翻页
- **Insert**，切换光标为输入/替换模式，光标将变成竖线/下划线
- **ESC**，退出输入模式，切换到命令模式

### 5.1.3 底线命令模式

在命令模式下按下 **:**（英文冒号）就进入了底线命令模式。

底线命令模式可以输入单个或多个字符的命令，可用的命令非常多。

在底线命令模式中，基本的命令有（已经省略了冒号）：

- `:w`：保存文件。
- `:q`：退出 Vim 编辑器。
- `:wq`：保存文件并退出 Vim 编辑器。
- `:q!`：强制退出Vim编辑器，不保存修改。

按 **ESC** 键可随时退出底线命令模式。

![img](https://www.runoob.com/wp-content/uploads/2014/07/vim-vi-workmodel.png)

## 5.2 vi 使用实例

```shell
$ vim runoob.txt
```

直接输入 **vi 文件名** 就能够进入 vi 的一般模式了。请注意，记得 vi 后面一定要加文件名，不管该文件存在与否！

# 6.yum(Yellow dug Updater,Modified)

yum 提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。

## 6.1 yum语法

```shell
yum [options] [command] [package ...]
```

- **options：**可选，选项包括-h（帮助），-y（当安装过程提示选择全部为 "yes"），-q（不显示安装的过程）等等。
- **command：**要进行的操作。
- **package：**安装的包名。

## 6.2 yum常用命令

- 1. 列出所有可更新的软件清单命令：**yum check-update**

- 2. 更新所有软件命令：**yum update**

- 3. 仅安装指定的软件命令：**yum install <package_name>**

- 4. 仅更新指定的软件命令：**yum update <package_name>**

- 5. 列出所有可安裝的软件清单命令：**yum list**

- 6. 删除软件包命令：**yum remove <package_name>**

- 7. 查找软件包命令：**yum search <keyword>**

- 8. 清除缓存命令:

  - **yum clean packages**: 清除缓存目录下的软件包
  - **yum clean headers**: 清除缓存目录下的 headers
  - **yum clean oldheaders**: 清除缓存目录下旧的 headers
  - **yum clean, yum clean all (= yum clean packages; yum clean oldheaders)** :清除缓存目录下的软件包及旧的 headers

# 7. apt(Advanced Packaging Tool)

apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器。

apt 命令提供了查找、安装、升级、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。

apt 命令执行需要超级管理员权限(root)。

## 7.1 apt 语法

```shell
 apt [options] [command] [package ...]
```

- **options：**可选，选项包括 -h（帮助），-y（当安装过程提示选择全部为"yes"），-q（不显示安装的过程）等等。
- **command：**要进行的操作。
- **package**：安装的包名。

## 7.2 apt常用命令

- 列出所有可更新的软件清单命令：**sudo apt update**

- 升级软件包：**sudo apt upgrade**

  列出可更新的软件包及版本信息：**apt list --upgradable**

  升级软件包，升级前先删除需要更新软件包：**sudo apt full-upgrade**

- 安装指定的软件命令：**sudo apt install <package_name>**

  安装多个软件包：**sudo apt install <package_1> <package_2> <package_3>**

- 更新指定的软件命令：**sudo apt update <package_name>**

- 显示软件包具体信息,例如：版本号，安装大小，依赖关系等等：**sudo apt show <package_name>**

- 删除软件包命令：**sudo apt remove <package_name>**

- 清理不再使用的依赖和库文件: **sudo apt autoremove**

- 移除软件包及配置文件: **sudo apt purge <package_name>**

- 查找软件包命令： **sudo apt search <keyword>**

- 列出所有已安装的包：**apt list --installed**

- 列出所有已安装的包的版本信息：**apt list --all-versions**

```shell
sudo apt update && sudo apt upgrade -y
#一键升级

sudo apt install mplayer --no-upgrade
#安装 mplayer 如果存在则不要升级

sudo apt install mplayer --only-upgrade
#如果只想升级，不要安装可以使用 --only-upgrade 
#只升级 mplayer，如果不存在就不要安装它

sudo apt install <package_name>=<version_number>
#设置指定版本，语法格式

sudo apt remove mplayer
#移除包

apt search libimobile
#查找名为 libimobile 的相关包

apt show pinta
#查看 pinta 包的相关信息

apt list --upgradeable
#列出可更新的软件包

sudo apt autoremove
#清理不再使用的依赖和库文件
```