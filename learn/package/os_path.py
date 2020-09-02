import os,pprint
# pprint.pprint(list(os.walk('E:\pycharm_len\py_learn\learn',topdown=False)))
for dir,_,paths in os.walk('E:\pycharm_len\py_learn\learn'):
    files = [os.path.join(dir,path) for path in paths]
    pprint.pprint(files)
