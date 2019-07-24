import os
os.chdir('/Users/Parshu/Documents/Python-P/python')
with open('word.txt','r') as f:
    sz=100

    k=f.read(sz)
    while len(k) > 0:
        print(f.tell())
        print(k)
        k=f.read(sz)
    count=0
    for i in k:
        
        if i.islower():
            count+=1
    print(count)