#! /usr/bin/env python3
"""
初始化项目目录结构
"""
import os
import sys

# 当前路径
base = os.path.dirname(os.path.abspath(__file__)) + '/'

def package_create(path):
    try:
        os.mkdir(path)
        with open(path+'/__init__.py','w') as f:
            ...
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'app'

    base_dir = base+name
    package_create(base_dir)
    try:
        with open(base_dir+'/main.py','w') as f:...
    except Exception as e:
        print(e)


    dirlst = ['api','crud','db','model','schema']
    for d in dirlst:
        package_dir = base_dir + '/' + d
        package_create(package_dir)
