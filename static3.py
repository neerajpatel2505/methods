# Neeraj Kumar

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    @staticmethod
    def incremented_salary(salary):
        salary = salary + 12000
        return("Incremented Salary is: ", salary)
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)
        print("Incremented Salary is: ", Employee.incremented_salary(self.salary))
        
    
        
obj = Employee("Neeraj",35,25000)
obj.display()