import re
import codecs
import func
# coding=utf-8
f = codecs.open("test1.lua","r+",'utf-8')
s1 = f.read()
print("读取的文件中的所以内容：\n",s1)
#处理文本
# # 1、匹配这种格式：     "...中文..."
# re_words = re.compile("\'[^\']*[\u4e00-\u9fa5]+[^\']*\'")
# mm = re_words.finditer(s1,0)
# func.pr(mm)
# for m_read in mm :
#     print("找出所有的符合字串：",m_read.group())
# m = re_words.sub(func.rrr,s1,0)
# print(m)
# # 2、匹配这种格式：     [[中文]]
# func.pl()
# re_words2 = re.compile("\[\[[\u4e00-\u9fa5]+\]\]")
# mm2 = re_words2.finditer(s1,0)
# func.pr(mm2)
# m2 = re_words2.sub(func.rrr2,s1,0)
# print(m2)
# f.seek(0,0)
# # 3、匹配这种格式：    --...
# func.pl()
# re_words3 = re.compile("\-{2}[^\n]*\n")
# mm3 = re_words3.finditer(s1,0)
# func.pr(mm3)
# 4、匹配这种格式：     [[...中文...]]   条件是：这个格式字符不在"--"的后面
# func.pl()
# re_words4 = re.compile("(?<=(string\=))\[\[.+\]\]")   #有个小bug，就是如果"--"注释在最后一行的话，则不会匹配为注释内容
# mm4 = re_words4.finditer(s1,0)
# # print(mm4)
# func.pr(mm4)
# m4 = re_words4.sub(func.rrr2,s1,0)
# print(m4)
# 5、匹配这种格式:       T(...)
# re_words5 = re.compile("T\([^\)]*\)")
# mm5 = re_words5.finditer(s1,0)
# func.pr(mm5)
# 6、匹配这种格式：       print_string()
# re_words6 = re.compile("print\_string\([^\)]*\)")
# mm6 = re_words6.finditer(s1,0)
# func.pr(mm6)
# 7、匹配这种格式：      log.*()
# re_words7 = re.compile("log\.[iedwf]\([^\)]*\)")
# mm7 = re_words7.finditer(s1,0)
# func.pr(mm7)
# 8、匹配这种格式：      --[[..]]
# re_words8 = re.compile("\-{2}\[{2}[^\[{2}]*\]\]")
# mm8 = re_words8.finditer(s1,0)
# func.pr(mm8)
# 9、匹配这种格式：      '[]'
# re_words9 = re.compile("\'\[.*\]\'")
# mm9 = re_words9.finditer(s1,0)
# func.pr(mm9)
# f.seek(0,0)
# f.truncate()#清空文件，只有当可以对该文件进行写操作时，该次函数才可使用
# print("s1:",s1,"------s1")
# f.write(m4)
# 10、匹配这种格式 ： "abf" ,要求""中间的内容不能包含中文，其他都匹配
# re_words10 = re.compile("\"[^\u4e00-\u9fa5\n\"]*\"")
# mm10 = re_words10.finditer(s1,0)
# func.pr(mm10)
# 11、匹配这种格式：'abf'，要求''中间的内容不能包含中文，其他都匹配
re_words11 = re.compile("\'[^\u4e00-\u9fa5\n\']*\'")
mm11 = re_words11.finditer(s1,0)
func.pr(mm11)
f.close()

