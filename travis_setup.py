#!/usr/bin/env python3
import os, shutil

os.mkdir('INGINIOUS-open')

dir = os.scandir('.')

for item in dir:
    if item.name != 'INGINIOUS-open' and (item.is_dir() or item.name == 'course.yaml'):
        try:
            os.mkdir(os.path.join(item.name,'test'))
        except:
            pass  # test directory already existing
        shutil.move('./' + item.name, 'INGINIOUS-open' + item.name)
