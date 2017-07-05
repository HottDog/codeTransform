import re
import codecs
import os
import sys
# coding=utf-8
#一些常量定义
# COMMON_PATH = "E:\\test_workspace\\First"
COMMON_PATH ="test2.lua"
#用到的函数
#T("")替换函数
def rrr(m):
    if m.group(11) != None :
        s=re.search("(?<=(\[\[))(.+)(?=(\]\]))",m.group(11),0)
        # print(s)
        # print("T(\""+s.group()+"\")")
        return "T(\""+s.group()+"\")"
    elif m.group(10)!=None:
        # print("T("+m.group(10)+")")
        return "T("+m.group(10)+")"
    elif m.group(9)!=None:
        # print("T("+m.group(9)+")")
        return "T("+m.group(9)+")"
    else:
        return m.group(0)

#处理单个文本函数
def processFile(file):
    try:
        f = codecs.open(file,"r+",'utf-8')
        s1 = f.read()
    except OSError:
        print("file's format is not utf-8")
#处理文本
#全格式匹配
# 需要忽视的点：
# a、--..          \-{2}[^\n]*\n
# b、--[[..]]        \-{2}\[{2}[^\[{2}]*\]\]
# c、T()               T\([^\)]*\)
# d、print_string()             print\_string\([^\)]*\)
# e、log.*()               log\.[iedwf]\([^\)]*\)
# f、'[]'               \'\[.*\]\'
# g、"sdasda"   说明：""中间为非中文的任意字符       \"[^\u4e00-\u9fa5\n\"]*\"
# h、 'sadas'   说明：''中间为非中文的任意字符       \'[^\u4e00-\u9fa5\n\']*\'
# 需要匹配的点：
# x、"..中文.."             \"[^\"]*[\u4e00-\u9fa5]+[^\"]*\"
# y、'..中文..'               \'[^\']*[\u4e00-\u9fa5]+[^\']*\'
# z、string=[[..]]             (?<=(string\=))\[\[.+\]\])  说明：获取到的结果只是[[]]，并没有获取string=
    re_words_all = re.compile("(\-{2}\[{2}[^\[{2}]*\]\])?"                    #b  2
                          "(\-{2}[^\n]*\n)?"                               #a  1
                          "(T\([^\)]*\))?"                                 #c  3
                          "(print\_string\([^\)]*\))?"                     #d  4
                          "(log\.[iedwf]\([^\)]*\))?"                      #e  5
                          "(\'\[.*\]\')?"                                   #f  6
                          "(\"[^\u4e00-\u9fa5\n\"]*\")?"                    #g  7   
                          "(\'[^\u4e00-\u9fa5\n\']*\')?"                    #h  8    
                                            #y  9
                          "(\"[^\"\n]*[\u4e00-\u9fa5]+[^\"\n]*\")?"         #x  10          
                            "(\'[^\'\n]*[\u4e00-\u9fa5]+[^\'\n]*\')?"                  
                                          #z  11
                          "(?(1)|(?(2)|(?(3)|(?(4)|(?(5)|(?(6)|(?(7)|(?(8)|(?(9)|(?(10)|((?<=(string\=))\[\[.+\]\])?))))))))))")    #说明：因为--..包含了--[[]]的一部分，所以--[[]]要先匹配
# mm_all = re_words_all.finditer(s1,0)
# func.pr(mm_all)
    m = re_words_all.sub(rrr,s1,0)
    f.seek(0,0)
    f.truncate()#清空文件，只有当可以对该文件进行写操作时，该次函数才可使用
    # print("s1:",s1,"------s1")
    f.write(m)
    f.close()

#遍历文件夹中的所有文件,并进行替换操作
#path 需要处理的文件夹的路径
def traverse(path):
    #如果是单个文件，则直接处理
    if not os.path.isdir(path):
        processFile(path)
        return
    #如果是文件夹则遍历处理
    files =os.listdir(path)
    for file in files:
        if not os.path.isdir(path+"\\"+file):
            #不是文件夹
            processFile(path+"\\"+file)
        else:
            # print('文件夹:'+path+"\\"+file)
            traverse(path+"\\"+file)

#获取命令行输入的参数
if len(sys.argv)>1:
    path = sys.argv[1]
    # url = view_constant.view_path + sys.argv[1] + view_constant.file_extension_lua
else:
    path = COMMON_PATH
traverse(path)
