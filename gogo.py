import re
import codecs
# coding=utf-8
f = codecs.open("test.lua","r+",'utf-8')
count =0
for line in f:
    if count<4:
        print(line,end='')
        count+=1
print("当前的文件指针位置：",f.tell())
f.seek(-20,1)
print(f.read(10))
print("当前的文件指针位置：",f.tell())
f.close()
f= codecs.open("test.lua","r+",'utf-8')
print("当前的文件指针位置：",f.tell())
s1=f.readline()
print(s1)
print("当前的文件指针位置：",f.tell())
f.seek(-10,1)
print("当前的文件指针位置：",f.tell())
print(f.read(10))
f.close()
