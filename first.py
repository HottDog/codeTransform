#!/user/bin/python
#-*- coding:UTF-8 -*-
import sys
import os
import chardet
if len(sys.argv)>1:
	print(str(sys.argv[1]))
else:
	print("请输入一个参数")
print("你好!")
a=False
if a:
	print("true")
else:
	print("false")
print("hah")
s = "Hello World!"
print(str(s))
print(repr(s))
print("12".zfill(6))
print("12".zfill(5).rjust(5))
print("12".ljust(5).zfill(5))
print("11","21","123","23",end='*')    #end='*'将原本默认的结尾换行符换成了自己定义的'*'
print("Good Bye!")
s1 = "hah"
s2 = s1
print(s2)
s2 = s2+"ss"
print(s2)
if s1 == "hah":
	print("字符串可以比较")
ssss = "jjaha "+"ss"
print(ssss)
# url = "E:\\test_workspace\\First"
url = "E:\\workspace\\chineseChessOverSea\\release\\xiangqi_android\\Resource\\scripts"
def traverse(path):
	files =os.listdir(path)
	for file in files:
		if not os.path.isdir(path+"\\"+file):
			print(file)
			try:
				f = open(path+"\\"+file,"rb+")
				result = chardet.detect(f.read())
				print("文件的编码格式：",result)
			except UnicodeDecodeError:
				print("UnicodeDecodeError")
		else:
			print('文件夹:'+path+"\\"+file)
			traverse(path+"\\"+file)

#判断该文件是否是lua后缀的文件,true为是
def isLuaFile(path):
	print(os.path.splitext(path)[1])
	if os.path.splitext(path)[1] == ".lua":
		return True
	else:
		return False

print(isLuaFile("test1.lua"))
# traverse(url)
# f=open("test2.lua","rb+")
# result = chardet.detect(f.read())
# print("文件的编码格式：",result)
# if result["encoding"] == "ISO-8859-1":
# 	print("这个文件是ISO-8859-1")
