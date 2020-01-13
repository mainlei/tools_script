#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# GitHub:https://github.com/mainlei/tools_script
# 分别打包两份png、plist 到指定的 ccb目录与工程目录 (不局限于此,可以定义为任何输出目录)
# 1.第一次运行脚本前必须安装TexturePacker并打开 
# 2.点击顶部菜单 "TexturePacker"--> "Install Command Line Tool"(安装命令行工作)
# 3.py脚本必须放到资源文件夹下
# 4.out_path_list 修改成自己的输出路径。如有跳过文件夹请配置 skips_list
# 5.执行目录 例如: python tp_output -p img
# 本脚本在Mac通过测试  Windows系统请自行配置TexturePacker命令

import os
import sys
import getopt

# -a 时候跳过的文件，这样的文件夹 在 -a 时候,skips_list内的文件夹不会被打包plist
skips_list = []
# 输出路径列表 可配置多个 使用当前的相对路径
out_path_list = ["ccb_path","pro_path"]
# ======================以上部分需要配置成自己的路径=======================


# 要打包的文件夹名 通过命令行 -p [path] 参数传入
path = ""
# -a 读取当前目录下所有文件夹
dir_list = []

# 提示
__doc__ = "可用的参数:\n -h         显示帮助信息\n -p [path]  打包指定文件名(*必须)\n -a 打包当前目录下的所有文件夹(需要跳过的文件请配置skips)"
# 全部打包标识
isAll = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:a")
    if len(opts) == 0:
        print "参数不可为空"
        print __doc__
        sys.exit(-2)
        pass
except getopt.GetoptError:
    # print help information and exit:
        print "getopt.GetoptError"
        print __doc__
        sys.exit(-2)

for o, a in opts:
    if o == "-h":
        # print help information and exit:
        print __doc__
        sys.exit(0)
    if o == "-p":
        path = a
        if path == '':
            print '错误：-p path 文件夹名不能为空'
            sys.exit(0)
    if o == "-a":
        isAll = True
        pass



if isAll:
    # print(os.listdir("."))
    paths = os.listdir(os.getcwd())
    for p in paths:
        if os.path.isdir(p):
            # print p+"it's a directory"
            dir_list.append(p)
            pass
else:
    if not os.path.exists(path):
        print "文件夹 [" + path + "]不存在"
        sys.exit(0)
        pass
    dir_list.append(path)
    pass


def out_texture(path):
    for outpath in out_path_list:
        # 输出都ccb
        out_path = outpath +"/"+ path
        print out_path
        # 此部分参数可以根据 TexturePacker 自行修改 文件格式也可以修改成.jpg等 
        cmd = "TexturePacker   --disable-rotation --data "+out_path+".plist --sheet "+out_path+".png --format cocos2d  "+path+"/*.png"
        err_code = os.system(cmd)
        pass


for path in dir_list:
    if skips_list.count(path):
        print "跳过文件夹[ "+path+" ]"
        continue
        pass
    print "======"+path+"======"
    out_texture(path)
    pass
