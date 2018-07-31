import os
ALLOW_FILE_TYPES = ('java','dart','py','js','md','json',)
def countLine(path=os.getcwd()):
    dirs = os.listdir(path)
    dirs = list(map(lambda x: os.path.join(path,x),dirs))
  
    line = 0
    for _dir in dirs:
        if os.path.isdir(_dir):
            line += countLine(_dir)
        else:
            file_type = _dir.split('.')[-1]
            if file_type in ALLOW_FILE_TYPES:
                with open(_dir,'r') as f:
                    line += len(f.readlines())
    return line
print('number of lines = {}'.format(countLine()))