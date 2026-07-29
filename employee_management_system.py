class Employee:

    employee_count = 0
    employee_list = []

    def __init__(self, employee_id, name , age):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        Employee.employee_count += 1
        Employee.employee_list.append(self)



    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


    def calculate_salary(self):
        pass        




class FullTimeEmployee(Employee):

    def __init__(self, employee_id, name, age, monthly_salary):
        super().__init__(employee_id, name, age)
        self.monthly_salary = monthly_salary


    def calculate_salary(self):
        return self.monthly_salary



class PartTimeEmployee(Employee):
    def __init__(self, employee_id , name , age , hourly_rate , hours_worked):
        super().__init__(employee_id, name, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked


    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked




class Freelancer(Employee):
    def __init__(self, employee_id , name , age , project_rate , projects_completed):
        super().__init__(employee_id, name, age)
        self.project_rate = project_rate
        self.projects_completed = projects_completed


    def calculate_salary(self):
        return self.project_rate * self.projects_completed








employee1 = FullTimeEmployee(1, "Akram ", 30, 5000)
employee2 = PartTimeEmployee(2, "Ahmad", 25, 20,   80)
employee3 = Freelancer(3, "Ashraf", 28, 1000, 5)




for employee in Employee.employee_list:
    employee.display_employee_info()
    print(f"Salary: {employee.calculate_salary()}\n")





total = 0
highest_salary = 0
highest_paid_employee = ""
for employee in Employee.employee_list:
    total = total + employee.calculate_salary()
    if employee.calculate_salary() > highest_salary:
        highest_salary = employee.calculate_salary()
        highest_paid_employee = employee.name




print("#############  Employees Report #############")


print("Total Employees:", len(Employee.employee_list))




print("Total payroll: ", total)


print("Highest paid employee: ", highest_paid_employee)



employee4 = PartTimeEmployee(4, "Nada",2 ,15 , 80 )


for employee in Employee.employee_list:
        print("Employee Name:", employee.name)



