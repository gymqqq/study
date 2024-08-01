# python 代码阅读

# 1.os库

```
The `os` module in Python is a built-in module that provides a way of using operating system dependent functionality. It allows your Python scripts to interact with the operating system, including tasks such as file I/O, process management, and environment variables.
```

## 1.1 方法

```python
一、os.mkdir("dir_name") #创建目录
os.rmdir("dir_name") #删除目录
os.chdir("dir_name") #改变当前工作目录
os.getcwd() #显示当前工作目录
os.listdir() #列出当前目录中所包含的文件
二、os.path常用方法
#__file__:This special variable in Python holds the path to the current script file. It's automatically set by the interpreter when you run a Python script.
1.os.path.splitext() #用于分离一个路径的文件名和扩展名
2.os.path.join(path1,path2,...) #用于将多个路径组合成一个路径
3.os.path.dirname(path) #用于返回一个路径的父目录路径
4.os.path.basename() #用于获取一个路径的文件名或最后一级目录名
5.os.path.exissts() #用于检查一个路径是否存在
6.os.path.isfile() #用于检查一个路径是否是文件
7.os.path.isdir() #用于检查一个路径是否是目录
8.os.path.abspath() #用于返回一个路径的绝对路径 (absolute path绝对路径，relative path 相对路径)
  os.path.abspath(__file__) #用于获取当前模块的绝对路径
```



## 1.2 方法实例

```python
一、
import os

# Get the current working directory
# 获取当前工作目录
print("当前的工作目录是："+os.getcwd())

os.rmdir('new_directory')
# Create a new directory
# 创建一个新的目录
os.mkdir('new_directory')

# 改变工作目录
# Change the current working directory
os.chdir('new_directory')

print("改变后的工作目录是"+os.getcwd())

#列出当前目录所包含的文件
# List the files in the current directory
print("目录中所包含的文件有：",end=' ')
print(os.listdir())
```

二、

~~~python
import os
2.
# 示例 1：组合两个绝对路径
path1 = '/path/to/dir'
path2 = '/path/to/file.txt'
print(os.path.join(path1, path2))  
# 输出：'/path/to/dir/path/to/file.txt'

# 示例 2：组合两个相对路径
path1 = './dir'
path2 = 'file.txt'
print(os.path.join(path1, path2))  
# 输出:'./dir/file.txt'

pritn(os.path.join("c:", "foo"))
#输出 c:foo 而不是 c:/foo

3.
# 示例 1：获取一个绝对路径的父目录
path = '/path/to/file.txt'
print(os.path.dirname(path))  # 输出：'/path/to'

# 示例 2：获取一个相对路径的父目录（如果此路径是相对路径，os.path.dirname() 会返回 '.'，表示当前目录）
path = './file.txt'
print(os.path.dirname(path))  # 输出：'.'

4.
# 示例 1：获取一个绝对路径的文件名
path = '/path/to/file.txt'
print(os.path.basename(path))  # 输出：'file.txt'

# 示例 2：获取一个相对路径的文件名
path = './file.txt'
print(os.path.basename(path))  # 输出：'file.txt'

5.
# 示例 1：检查一个绝对路径是否存在
path = '/path/to/file.txt'
print(os.path.exists(path))  # 如果文件存在，输出：True，否则输出：False

# 示例 2：检查一个相对路径是否存在
path = './file.txt'
print(os.path.exists(path))  # 如果文件存在，输出：True，否则输出：False

8.
# 获取一个相对路径的绝对路径
rel_path = './file.txt'
abs_path = os.path.abspath(rel_path)
print(abs_path)  # 输出：'/path/to/file.txt'

# 获取一个绝对路径的绝对路径
abs_path = '/path/to/file.txt'
print(os.path.abspath(abs_path))  # 输出：'/path/to/file.txt'
~~~

## 1.3 config实例

~~~python
import os
#获取当前文件的绝对路径，然后获取该绝对路径的父目录路径
cur_dir = os.path.dirname(os.path.abspath(__file__))
#获取当前文件的父路径的父路径
src_dir = os.path.dirname(cur_dir)
#获取当前文件的父路径的父路径的父路径
base_dir = os.path.dirname(src_dir)
#目录的绝对路径
embedding_path = 'D:/Code/Android_new/model/embedding/bge-large-zh-v1.5'
#相当于创建一个新的目录base_dir:\data
data_dir = os.path.join(base_dir, 'data')
#在该目录下创建2个文件，一个knowledge.txt,一个knowledge.pkl
knowledge_txt_path = os.path.join(data_dir, 'knowledge.txt')
knowledge_pkl_path = os.path.join(data_dir, 'knowledge.pkl')
#相当于创建一个新的目录base_dir:\log
log_dir = os.path.join(base_dir, 'log')
#在该目录下创建一个文件，log.log
log_path = os.path.join(log_dir, 'log.log')

~~~

> [!IMPORTANT]
>
> 本实例代码中，运用了os模块，且所有的路径均为绝对路径，每一次操作都是在绝对路径进行。

# 2.pickle库

```
"Pickle"库在Python中是一个非常有用的库，用于实现对象的序列化和反序列化。
序列化指的是将一个Python对象转换成字节流的过程，以便它可以被存储在文件或通过网络传输。
反序列化则是相反的过程，即将字节流转换回原来的Python对象。这使得Python对象可以跨会话持久保存和传输。
```

## 2.1 方法

```python
Pickle库的基本使用
序列化（Pickle）：
pickle.dump() #函数将Python对象序列化存储到文件中，或者使用pickle.dumps()将Python对象序列化为字节对象。
反序列化（Unpickle）：
pickle.load()  #函数从文件中读取并反序列化Python对象，或者使用
pickle.loads() #将字节对象反序列化回Python对象。

理解序列化的一个更直接的方式是将其想象成一个将复杂对象转换成可传输或可存储格式的过程。可以把它想象为打包或编码数据的过程，以便于存储到文件中或通过网络发送给其他程序，而后可以再将这个格式“解包”或解码回原始的对象。

举个简单的比喻：假设你有一盒玩具（这里的玩具代表数据中的复杂对象），你需要将这盒玩具寄给住在另一个城市的朋友。直接寄送整盒玩具可能不太方便，所以你决定将玩具拆开，分类打包（序列化），然后通过邮件发送。当你的朋友收到这些包裹后，根据你的说明（序列化的格式），他能够将这些玩具重新组装（反序列化）成原来的样子。
```

## 2.2 方法实例

```python
###序列化
import pickle

# 创建一个示例字典数据
data = {'a': [1, 2.0, 3, 4+6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}}

# 将数据序列化并写入文件
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
```



```python
###反序列化
import pickle

# 从文件中读取并反序列化数据
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)
```

# 3.loguru库

## 3.1 方法

~~~python
提供了一种简单的日志记录方法，旨在替代Python标准的logging模块。
通过简化日志记录的设置和使用过程，Loguru让开发者能够更加轻松地捕获和记录程序运行时的信息。
它提供了许多便利的功能和改进，使得日志记录变得更加直观和强大。
~~~

~~~python
from loguru import logger

logger.debug("这是一个debug信息")
logger.info("这是一个info信息")
logger.warning("这是一个warning信息")
logger.error("这是一个error信息")
~~~

## 3.2 方法实例

~~~python
#记录到文件并设置日志旋转：
from loguru import logger

logger.add("file_{time}.log", rotation="1 week")  # 每周旋转日志文件
logger.info("这些信息将被记录到文件中")
~~~

~~~python
#捕获并记录异常：
from loguru import logger

def my_function(x):
    return 1 / x

try:
    my_function(0)
except ZeroDivisionError:
    logger.exception("哦不，发生了一个异常！")
~~~

# 4.sentence_transformers 库

## 4.1 方法

```
sentence_transformers是一个基于PyTorch的Python库，用于方便地生成句子级别的嵌入表示。
它是在Hugging Face的transformers库之上构建的，后者提供了对多种自然语言处理（NLP）任务有用的预训练模型，如BERT、RoBERTa、GPT等。sentence_transformers库特别优化了这些模型以改进句子或段落级别的表示，使其非常适合于诸如句子相似性计算、聚类、信息检索等任务。
```

## 4.2 方法实例

~~~python
#sentence_transformers来生成句子嵌入：
from sentence_transformers import SentenceTransformer

# 加载预训练模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 定义句子
sentences = ['This is an example sentence', 'Each sentence is converted']

# 生成嵌入向量
sentence_embeddings = model.encode(sentences)

# 输出嵌入向量
for sentence, embedding in zip(sentences, sentence_embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding[:5])  # 打印前5个维度作为示例
~~~

> [!TIP]
>
> `sentence_transformers`非常适合于需要句子级别语义理解的场景，例如：
>
> - **句子相似度**：计算两个句子的语义相似度。
> - **句子聚类**：基于语义相似度将句子分组。
> - **信息检索**：在大量文本中找到与查询最相关的句子。
> - **问答系统**：找到与用户问题最匹配的答案。
>
> 此库利用最新的NLP技术，为开发者提供了一个强大的工具来处理涉及句子表示的复杂任务。

# 5.encode实例

~~~python
import pickle
from loguru import logger
from sentence_transformers import SentenceTransformer
import sys
import os
import asyncio #异步协程
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#这行代码将当前文件的父目录添加到 Python 的模块搜索路径中，使得可以导入同级目录下的模块。
#通俗的可以理解为追溯到D:/filename 相当于global directory
from config.config import embedding_path
from config.config import knowledge_txt_path, knowledge_pkl_path


def load_embedding() -> SentenceTransformer:
    logger.info('Loading embedding...') #通知信息
    emb = SentenceTransformer(embedding_path) #加载预训练模型
    logger.info('Embedding loaded.') #通知信息
    return emb


def encode():
    emb = load_embedding()  #调用方法
    with open(knowledge_txt_path, 'r', encoding='utf-8') as f:
        read_lines = f.readlines()
    #f.readlines() is a method in Python that reads all the lines in a file and returns them as a list of strings.
    
    lines = []
    for line in read_lines:
        line = line.strip() #用于移除 line 的前导和尾随空白。
        temp = line.split(',')[0] #line是一句话，然后按'，'分隔开，会变成一个列表，取列表第一个数
        temps = ['北航', '博物馆', '航博', '校史馆','杭州','中法航空学院']
        if not any(t in temp for t in temps): #作比较的时候使用
        #if 条件为真往下走，条件为假跳过
        #if not 条件为真跳过，条件为假往下走
        #可快速判断一个集合中的任何元素是否存在于另一个字符串或集合中。
        #即可快速判断temp中的任何元素是否存在于temps中。
        #即如果该条没有北航，则在每一条前面加上北航
        #temp只有是一个小短句，temps是一个列表，看看小短句和列表中是否有相同的元素
            line = '北航' + line
        lines.append(line) #把修改后的line或者未修改的line都加到lines列表当中
        
    encoded_knowledge = emb.encode([line for line in lines]) #生成嵌入向量
    #括号中的line for line in lines相当于是对每一句话生成嵌入向量
    with open(knowledge_pkl_path, 'wb') as f:
        pickle.dump(encoded_knowledge, f)#序列化

if __name__ == '__main__':
    encode()
    print("task done!")
~~~

