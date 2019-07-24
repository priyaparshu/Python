import os
from datetime import datetime


#os.chdir('/Users/Parshu/Documents/Python-P/python')
#print(dir())
#print(os.listdir())
#os.mkdirs os.mkdir()
#os.removedirs and os.rmdir()
#os.rename('orig name','new name')
# st=os.stat('/Users/Parshu/Documents/Python-P/python/word.txt').st_mtime
# print(datetime.fromtimestamp(st))

# dirt = list(os.walk('/Users/Parshu/Documents/Python-P/python/'))
# print(dirt)
# k =os.environ.get('SHELL')
# print(k)

# l = os.path.join(os.environ.get("SHELL") , "word.txt")
# p = print(os.getcwd())
# print(p)
l = os.path.join(os.getcwd(),"word.txt")
r = os.path.basename(l)
d = os.path.dirname(l)
s = d = os.path.split(l)

# if (os.path.exists(l)):
#     print('yyyyyy')
# else:
#     print('nnnnnn')

# g =os.path.isdir(l)
# h = os.path.isfile(l)
# h = os.path.splitext(l)

print(dir(os.path))