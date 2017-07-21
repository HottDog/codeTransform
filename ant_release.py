# coding=utf-8
import os
import shutil

MOVE_SCRIPT = "\\Resource\\scripts"
MOVE_IMAGE = "\\Resource\\images"
DELETE_SCRIPT = "\\assets\\scripts"
DELETE_IMAGE = "\\assets\\images"

def deleteFile(path):
    if os.path.exists(path):
        shutil.rmtree(path)


android_workspace = os.getcwd()   #脚本当前所在的工作目录
android_workspace_top = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))   #脚本上一层的工作路径
# print(android_workspace_top)
deleteFile(android_workspace+DELETE_IMAGE)
print("delete "+android_workspace+DELETE_IMAGE)
deleteFile(android_workspace+DELETE_SCRIPT)
print("delete "+android_workspace+DELETE_SCRIPT)
shutil.copytree(android_workspace_top+MOVE_IMAGE,android_workspace+DELETE_IMAGE)
print("copy "+android_workspace_top+MOVE_IMAGE+" to "+android_workspace+DELETE_IMAGE)
shutil.copytree(android_workspace_top+MOVE_SCRIPT,android_workspace+DELETE_SCRIPT)
print("copy "+android_workspace_top+MOVE_SCRIPT+" to "+android_workspace+DELETE_SCRIPT)
os.system("ant clean")
os.system("ant release")
