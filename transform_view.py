import re
import codecs
import sys
import view_constant
# coding=utf-8
#用到的函数
#T("")替换函数
def rrr2(m):
    if m.group(2) != None :
        s=re.search("(?<=(\[\[))(.+)(?=(\]\]))",m.group(2),0)
        # print(s)
        # print("T(\""+s.group()+"\")")
        return "T(\""+s.group()+"\")"
    else:
        return m.group(0)
#获取命令行输入的参数
if len(sys.argv)>1:
    url = view_constant.view_path + sys.argv[1] + view_constant.file_extension_lua
else:
    url = view_constant.view_path + view_constant.own_view_new + view_constant.file_extension_lua
f = codecs.open(url,"r+",'utf-8')
s1 = f.read()
re_words4 = re.compile("(\-{2}[^\n]*\n)?(?(1)|(\[\[.+\]\]))")   #有个小bug，就是如果"--"注释在最后一行的话，则不会匹配为注释内容
m4 = re_words4.sub(rrr2,s1,0)
f.seek(0,0)
f.truncate()#清空文件，只有当可以对该文件进行写操作时，该次函数才可使用
f.write(m4)
f.close()
