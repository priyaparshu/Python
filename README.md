# Python

In this example we will create an Employee class and then create an instance of the class. we will get input from user and create a list of users. we will then save the list to a file and then read it back later.

We will be using a python module called pickle.We don't have to install - it ships with Python. And what I've done here is I've created an instance of the class.Pickle module serializes objects so they can be saved to a file, and loaded in a program again later on.

wb stands for write binary. That's very important. Otherwise, things don't work because pickle is a binary format. So, we'll open this file. We're going to create it. It doesn't exist yet.we use the pickle module, and we call dump on it. So, the first argument here is the object we are passing in, which is the class instance; and the second argument is a file; and that's how you pickle an object - writing it to a file, in this case. 

unpickle an object means to read it back from the file and get it back into memory.



