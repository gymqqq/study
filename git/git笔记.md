## 1.版本库

新建版本库：对本地代码进行管理
版本库(仓库)  可理解为一个目录
repository

> [!NOTE]
>
> 创建仓库：
> 方式一：git init [name]
> 方式二：git clone [url]

~~~shell
git init my-repo
my-repo文件夹作为仓库
~~~

## 2.工作区域

### 工作区

Working Directory 自己电脑上的目录

- 实际操作的目录

### 暂存区

Staging Area 临时存储区，保存即将上传git的命令

- 中间区域，用来临时存放即将提交的修改内容

### 本地仓库

包含了完整的项目历史和元数据

- git存储代码和版本信息的主要位置

   ls           git ls-files
   工作区 --> 暂存区 -->本地仓库
       git add        git commit

## 3.文件状态

![image-20240730090844258](.\images\image-20240730090844258.png)

已经加到暂存区的拿出来: git rm --cached <file>

提交暂存区的文件 git commit -m "parameter"

~~~shell
git status #查看状态
git status -s(short) ?? (暂存区工作区)

git add *.txt #添加所有以.txt结尾的文件进入暂存区
git add . #添加所有未跟踪的文件进入暂存区
git commit -m "parameter"
git commit #进入vim，第一行输入注释保存即可
git log --oneline #查看简洁的提交记录
~~~

## 4.git reset回退

![0774a48347b3b02c281950c60a544cf](.\images\0774a48347b3b02c281950c60a544cf.png)

~~~shell
git reset --soft/hard/mixed HEAD^/[ID]
#HEAD表示现在的指针，HEAD^表示前一个HEAD，回退到前一个版本
git reflog #查看所有操作命令
git reset --hard 版本号 可回退之前的版本
~~~

## 5.git diff查看版本差异

~~~shell
git diff #比较工作区和暂存区 红色删除 绿色添加
git diff HEAD #比较工作区和版本库
git diff --cached #比较暂存区和版本库
git diff ID1 ID2 #比较两个特定版本的差异
git diff HEAD~[number] HEAD #HEAD之前的number个版本
git diff HEAD~[number] HEAD file.txt #之、只查看file.txt的差异内容
~~~

## 6.git rm 删除文件

~~~shell
#四种删除方法
1.
rm file.txt #在工作区删除文件
git status  #查看此时状态
git add file.txt  #将删除文件的信息告诉暂存区
2.
git rm file.txt #直接在工作区和暂存区删除文件
3.
git rm --cached <file> #在暂存区删掉，但保留在当前工作区中
4.
git rm -r * #递归删除某个目录下的所有子目录和文件

git commit -m ""  #最后一定要运行一下，告诉版本库删除文件了
~~~

## 7. .gitignore文件

![image-20240730094019811](.\images\image-20240730094019811.png)

![image-20240730094452363](.\images\image-20240730094452363.png)

![image-20240730094517779](.\images\image-20240730094517779.png)

## 8.配置SSH密钥

~~~shell
cd ~
cd .ssh
ssh-keygen -t ras -b 4096
enter #第一次使用 继续enter
输入test
enter
ls -ltr
#test     私钥文件
#test.pub 公钥文件
tail -5 config #加入下面5行
# github
Host github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/test
~~~

~~~shell
命令行指令ls, 列出目录(文件夹)下文件, ls for list
  -l, 以每行一个的格式列出文件, l for long
  -a, 列出包含隐藏文件的所有文件, a for all
  -S, 以文件大小顺序列出文件, S for Size
  -t, 以修改日期顺序列出文件, t for time modified
  -r, 以倒序列出文件，r for reverse
  参数可以叠加，ls-ltr就是每行一条以文件修改日期倒序排列列出文件
~~~

## 9.git push/git pull

~~~shell
git push#把本地仓库的修改推送给远程仓库
git pull#把远程仓库的修改拉取到本地仓库
git clone [url] #克隆
~~~

## 10.关联本地仓库和远程仓库

~~~shell
git remote add <shortname> <url>
#一般默认<shortname>为origin
#<url>:git@github.com:gymqqq/first-repo.git
git remote -v #查看当前仓库所对应的远程仓库的别名和地址
git branch -M main #指定分支的名称为main
git push -u origin main:main #吧本地仓库的main和别名为origin的远程仓库关联起来

#更改远程仓库的修改
git pull <远程仓库名> <远程分支名>:<本地分支名>

#在执行完git pull后，Git会自动为我们执行一次合并操作，如果远程仓库中的修改内容和本地仓库中的修改内容没有冲突的话，那么合并操作就会成功，否则合并操作就会由于冲突而失败，这个时候我们就需要手动来解决冲突。
#从远程仓库获取内容还可以使用fetch命令，fetch命令只是获取远程仓库的修改，但是并不会合并到本地仓库中，而是需要我们手动合并。
~~~

## 11.分支

~~~shell
git branch #查看分支
git branch name #创建新的分支

git checkout name #切换到新的分支
git checkout name #恢复文件到之前的版本 
git checkout  -b name ID #恢复到name在ID时的版本
git checkout #默认切换分支，而不是恢复文件

git switch #用来专门切换分支

#合并分支（dev分支合并到main分支）
git switch main
git merge dev

#查看分支图
git log --graph --oneline --decorate --all
alias grapu="git log --graph --oneline --decorate --all"#定义别名

git branch -d dev #-d表示删除已经完成合并的分支
git branch -D dev #-D表示删除未完成合并的分支
~~~

## 12. 解决合并冲突（git merge合并）

~~~shell
git branch feat #feature的简写，一般表示开发某一个功能的分支
git commit -a -m "parameter" #一个命令完成暂存和提交两个操作
git diff #可以查看冲突的具体内容
#如果某个文件合并时有冲突，则需要手动编辑一下冲突的文件
#合并后，文件内容会合并，但是合并会有冲突，需要手动编辑一下冲突的文件
#改完以后，提交，会自动完成合并的过程
git merge --abort #可以在合并过程中中断合并
~~~

## 13. Rebase合并分支

~~~shell
git rebase branch-name #rebase可以理解为合并到xx

git switch dev #切换到dev分支
git rebase main #合并到main分支

#git中，每个分支都有一个指针，指向当前分支的最新提交记录
#执行rebase时，git会先找到当前分支和目标分支的共同祖先，从祖先开始移动合并
~~~

> [!NOTE]
>
> Merge：只想合并 不关心提交历史 
>
> ​	指针合在一起
>
> ​	优点：不会破坏原分支的提交历史，方便回溯和查看
>
> ​	缺点：会产生额外的提交节点，分支图比较复杂
>
> Rebase：只有自己一个人开发 并且要提交历史清晰明了
>
> ​	挪到一起，变成一根线
>
> ​	优点：不会新增额外的提交记录，形成线性历史，比较直观和干净
>
> ​	缺点：会改变提交历史，改变了当前分支branch out的节点。避免在共享分支使用

