import re
url = "www.ruobi.com"
s1 = re.match('w[^1-10]w',url).group()
s2 = re.match("com",url)
s3 = re.search("com",url)
s4 = re.search("^w.*m$",url)
print(s1)
print(s2)
print(s3.span())
print(s4.group())
ss = "sshdjjgaabfa+sds0213    \\\\      \   我们都市众人过     --   haha  哈哈"
re_words = re.compile("[\u4e00-\u9fa5]+")
m = re_words.search(ss,0)
print(m.group())