# Python

In this example I am creating an Employee class and then I created an instance of the class. I will get input from user and create a list of users and save the list to a file. I  then read it back.

I am using a python module called pickle. It ships with Python. Pickle module serializes objects so they can be saved to a file, and loaded in a program again later on.

wb stands for write binary. That's very important. Otherwise, things don't work because pickle is a binary format. I use the pickle module and I call dump function on it. The first argument is the object i need to pass in, (which is the class instance); and the second argument is a file; and that's how we pickle an object - writing it to a file, in this case. 

unpickle an object means to read it back from the file and get it back into memory.



