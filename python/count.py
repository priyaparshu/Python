import os
l = os.path.join(os.getcwd(),'word.txt')

def make_dict(s):
    w_dict = {}
    word_list = s.split()
    #print(word_list)
    for wrd in word_list:
        #print("wrd",wrd)
        w_dict[wrd] = w_dict.get(wrd,0)+1
        #print("w_dict[wrd]",w_dict[wrd])
    return w_dict
dc = make_dict(python3 readfile(python3 l ))
print(dc)