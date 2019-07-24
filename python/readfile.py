import os
def readfile():
    l = os.path.join(os.getcwd(),"word.txt")
    print(l)
    with open(l,"r") as f:
        size_to_read=10
        wordstr = f.read(size_to_read)
        print(f.tell())
        # while len(wordstr) > 0:
        #     print(wordstr,end='*')
        #     wordstr = f.read(size_to_read)
    return wordstr
readfile()
