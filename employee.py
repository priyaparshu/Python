import pickle
import os
os.chdir(os.getcwd())
class Employee:
    def __init__(self,name="",title="",salary=0):
        self.name=name
        self.title=title
        self.salary=salary
    
    
    def __str__(self):
      s="Employee:"
      s += ('(' + self.name + ',' + self.title + ',' + str(self.salary )+ ')')
      return s


    def create_list(self):
            emp_rec =[]
            
            
            while True:
                name_n = input('Enter name: ')
                if not name_n:
                        return emp_rec 
                title = input('Enter title: ')
                salary = int(input('Enter salary: '))
                emp_info = Employee(name_n, title, salary)
                emp_rec.append(emp_info)
            return emp_rec

    def save_data(self,fname,a_list):
        # a_list = create_list()
        with open(fname,"wb") as f:
            pickle.dump(a_list,f)
    
    def load_data(self,fname):
        with open(fname,"rb") as f:
            alist = pickle.load(f)
        for i in a_list:
            print(i)
        
# print('This is the record for %s.' %empl1)

emp = Employee()
a_list = emp.create_list()
emp.save_data('data.txt',a_list)
emp.load_data('data.txt')
# for i in data:
#     print(i)

