import os
for i in os.listdir():
    print(i)
l = os.path.join(os.getcwd(),"word.txt")
fn,extn = os.path.split(l)
print(fn)
print(extn)
l = os.path.join(os.getcwd(),"word.txt")
w=os.path.join(os.getcwd(),"test.txt")

f_title
f_title
def copr():
    with open(l,'r') as wr:
        with open(w, 'a') as ww:
            for ln in wr:
                ww.write(ln)

copr()