import time
import random

names = ["John","Corey","Adam","Steve","Rick","Thomas"]
majors=["Math","CompSci","Engineering","Arts","Business"]

def person(n):
    
    result = []
    for i in range(n):
        
        personal =   {
        
            'id':i,
            'name':random.choice(names),
            'major': random.choice(majors)
            }
            
        result.append(personal)

    return result

res = person(5)
for i in res:
    print(i)

