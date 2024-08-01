# shell脚本教程

# 1.Bourne Again Shell(bash)

> [!TIP]
>
> 在一般情况下，人们并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 **#!/bin/sh**，它同样也可以改为 **#!/bin/bash**。

## 1.1 第一个shell脚本

~~~shell
#!/bin/bash
echo "Hello World !"
#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。
# echo 命令用于向窗口输出文本。
~~~

## 1.2 运行shell脚本

### 1.2.1 作为可执行程序

![image-20240728093642722](C:\Users\31958\AppData\Roaming\Typora\typora-user-images\image-20240728093642722.png)

创建一个sh文件，然后向其添加"x"权限，接着直接使用名称运行。
写成./test.sh是因为如果写成test.sh，系统会去PATH里找，但是当前目录是不在PATH里的。所以需要在test.sh前加./以表示当前目录下的文件。

### 1.2.2 作为解释器参数

> [!NOTE]
>
> 直接运行解释器，其参数就是 shell 脚本的文件名

![image-20240728094233606](C:\Users\31958\AppData\Roaming\Typora\typora-user-images\image-20240728094233606.png)

# 2.Shell变量

可以直接设置变量。

## 2.1 使用变量

~~~shell
your_name="gaiyiming"
echo {your_name}
echo ${your_name}
~~~

变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界

![image-20240728095309280](C:\Users\31958\AppData\Roaming\Typora\typora-user-images\image-20240728095309280.png)

> [!TIP]
>
> 推荐给所有变量加上花括号，这是个好的编程习惯。

~~~shell
只读变量: readonly + 变量名
删除变量：unset + 变量名
整数变量：declare/typeset + -i + 变量名
数组变量：
	整数索引数组：
	   my_array=(1 2 3 4 5)
	关联数组：
	   declare -A associative_array
	   associative_array["name"]="John"
	   associative_array["age"]=30
特殊变量：
	有一些特殊变量在 Shell 中具有特殊含义，例如 $0 表示脚本的名称，$1, $2, 等表示脚本的参数。$#表示传递给脚本的参数数量，$? 表示上一个命令的退出状态等。
~~~

## 2.2 字符串

单引号字符串的限制：

- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
- 单引号字符串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

双引号的优点：

- 双引号里可以有变量
- 双引号里可以出现转义字符

![image-20240728100837116](C:\Users\31958\AppData\Roaming\Typora\typora-user-images\image-20240728100837116.png)