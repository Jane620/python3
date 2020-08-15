import os
import pathlib

def dir(path):
    for x in os.listdir(path):
        print(f"x is {x}")
        dirInfo = os.stat(x)
        nextDir = os.path.join(path, x)
        print(f'当前文件%s绝对路径为：{(x,nextDir)}')
        dirType = dirInfo.st_mode & 0o170000
        print(f'文件类型代码：{dirType}')
        #os.chdir(nextDir)
        dir(nextDir)

Dirpath=pathlib.Path(pathlib.Path.cwd()).resolve()
print(f"dir is {Dirpath}")
dir(Dirpath)