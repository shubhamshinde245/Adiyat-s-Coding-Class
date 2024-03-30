class Employee:
    count = 0

    def __init__(self, name , position, salary) -> None:
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1
    
    def displayCount(self):
        print("Total employees : ", Employee.count)
    
    def displayInfo(self):
        print("Name :{0}, Position :{2}, Salary :{1}".format(self.name, self.salary, self.position))

emp1 = Employee("Employee 1", 'HR', "40,000")

name = input("Enter name :")
position = input("Enter position :")
salary = input("Enter salary :")

emp2 = Employee(name, position, salary)
emp2.displayInfo()
emp1.displayCount()