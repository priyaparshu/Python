class StackOverflowUser:
        def __init__(self, name="", userid=0, rep=0): 
            
            self.name = name
            self.userid = userid
            self.rep = rep
        
        def __str__(self):
            s="Employee:"
            s += ('(' + self.name + ',' + str(self.userid) + ',' + str(self.rep )+ ')')
            return s  


        
        def dataentry(self):
            daven = []
            while True:
                name = input("Enter name: ")
                if not name:
                    return daven
                    
                
                userid = int(input("Enter user id: "))
                rep = int(input("Enter rep: "))
                dave = StackOverflowUser(name, userid, rep)
                daven.append(dave)
            return daven
                
            
d = StackOverflowUser()
data=d.dataentry()
for i in data:
    print(i)

