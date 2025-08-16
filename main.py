#HOME PAGE
from utility import option, Manager

manager = Manager("database.db") 

print("Welcome User")
print("This Program is to help you manage your daily tasks")

print(option())
n = int(input("Enter 1/2/3/4 according to their corresponding functions: "))

if n == 1 :
    task = input("Enter task name:")
    manager.add(task)
    
elif n == 2 :
       '''add function 2 here'''
    
elif n == 3 :
       '''add function 3 here'''
    
elif n == 4 :
       '''add function 4 here'''
    
else :
      print("Please enter right option number")       
