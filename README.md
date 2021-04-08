# DBaseALL
> 一道题没看出来是Base58，最后看着汇编把Base58编码算法都写出来了,还是没看出来……还是经验太少了
> 看着没什么现成的好用的轮子，有个类似的BaseCrack可是不能 translate 。在前面虽然也可以，但是还是自己搓个吧。

尝试自动解码Base16-Base92，可以替换alphabet，并自动标识正常字符和Flag
![image](https://user-images.githubusercontent.com/49470951/113964453-1d3fcb80-985e-11eb-9eba-b2b40f6b408d.png)
![image](https://user-images.githubusercontent.com/49470951/113964647-80316280-985e-11eb-8c64-3e5e7e431f3b.png)

可以通过命令行参数调用
```Shell
>> python BaseAll.py ZmxhZ2FzZGZhc2RmYXNkZg== 
>> python BaseAll.py ZmxhZ2FzZGZhc2RmYXNkZg== {alphabet}
```
也可以直接启了以后在输入
```Shell
>> python BaseAll.py
██████╗     ██████╗  █████╗ ███████╗███████╗ █████╗ ██╗     ██╗
██╔══██╗    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║     ██║
██║  ██║    ██████╔╝███████║███████╗█████╗  ███████║██║     ██║
██║  ██║    ██╔══██╗██╔══██║╚════██║██╔══╝  ██╔══██║██║     ██║
██████╔╝    ██████╔╝██║  ██║███████║███████╗██║  ██║███████╗███████╗
╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝  w12

Can use args to do it. Like: BaseAll.py ZmxhZ2FzZGZhc2RmYXNkZg== {{alphabet}}
Input need decode string >> 
Input new Alphabet (Can don't input to use Default) >>
```

给到的alphabet 是根据**长度**判断对应 然后进行对应转换后 对应解码
```python
for index,oneAb in enumerate(self.baseAbDict):
    if newAlphabetLen == len(oneAb):
        # 尝试转换后进行decode
        print('May '+self.infoList[index]+' alphabet. Try to Translate And Decode:')
        trans = str.maketrans(alphabet,self.baseAbDict[index])
       # 尝试对应解码
       res = self.baseDecodeFunc[index](decodeStr.translate(trans))
```
