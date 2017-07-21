# coding=utf-8
import os
import re
import codecs
import func
import view_constant
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

def processFile(file):
    fileFormat = func.getFileFormat(file)
    f = codecs.open(file,"r+",fileFormat)




url = ""
