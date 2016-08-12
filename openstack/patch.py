#-*- coding:utf-8 -*-
import re
import os

def patch_md(filename):
    if filename.endswith('.md'):
        return True
    return False

def _patch_replace(text):
    pattern=re.compile(r'(?<=!)\[.*\]\((.*)(?=\))')
    result = re.findall(pattern,text)
    print result
    for filedir in result:
        print '==================================='
        if '\\' in filedir:
            listfile = filedir.split('\\')
        else:
            listfile = filedir.split('/')
        pattern_file = r'(?<=!)\[.*\]\(.*[\\/]+(?='+listfile[-1]+r'\))'
        pattern_repl=re.compile(pattern_file)
        result = re.findall(pattern_repl,text)
        print result
        replace_file=r'[](https://github.com/C2python/opentsack-conf/blob/master/openstack/img/'#TTTTTT换成[](http://github.com/C2python/openstackconf/openstack/img
        text=re.sub(pattern_repl,replace_file,text)
        print listfile[-1]
        print '==================================='
    return text

def patch_replace(filename):
    print filename
    with open(filename,'r+') as f:
        text=f.read()
        text_file=_patch_replace(text)
        #print text
    with open(filename,'w') as f:
        f.write(text_file)
        #print text_file


def run():
    dirpath = raw_input("输入所要处理的文件的目录：")
    fileset = filter(patch_md,os.listdir(dirpath))
    print fileset
    for filename in fileset:
        absfile = os.path.join(dirpath,filename)
        patch_replace(absfile)

if __name__=='__main__':
    run()