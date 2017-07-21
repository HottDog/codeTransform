# coding=utf-8
import os
import difflib
import argparse
import sys
import chardet
COMMON_PATH = "E:\\test_workspace\\Util\\"
def getFileFormat(file):
    f=open(file,"rb+")
    result = chardet.detect(f.read())
    # print("文件的编码格式：",result)
    # if result["encoding"] == "ISO-8859-1":
    # print("这个文件是ISO-8859-1")
    f.close()
    return result["encoding"]
# 创建打开文件函数，并按换行符分割内容
def readfile(filename):
    try:
        with open(filename, 'r',encoding="utf8") as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()

# 比较两个文件并输出到html文件中
def diff_file(filename1, filename2):
    text1_lines = readfile(filename1)
    text2_lines = readfile(filename2)
    d = difflib.HtmlDiff()
    # context=True时只显示差异的上下文，默认显示5行，由numlines参数控制，context=False显示全文，差异部分颜色高亮，默认为显示全文
    result = d.make_file(text1_lines, text2_lines, filename1, filename2, context=True)
    # 内容保存到result.html文件中
    with open('result.html', 'w') as resultfile:
        resultfile.write(result)
        # print(result)


if __name__ == '__main__':
    # 定义必须传入两个参数，使用格式-f1 filename1 -f2 filename
    parser = argparse.ArgumentParser(description="传入两个文件参数")
    parser.add_argument('-f1', action='store', dest='filename1', required=True)
    parser.add_argument('-f2', action='store', dest='filename2', required=True)
    given_args = parser.parse_args()
    filename1 = given_args.filename1
    filename2 = given_args.filename2
    diff_file(filename1, filename2)
    # diff_file(COMMON_PATH+"1.txt", COMMON_PATH+"11.txt")