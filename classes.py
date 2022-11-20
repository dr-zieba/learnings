class emp:
    def get_name_age_salary(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        return None

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        return None


emp1 = emp()
emp2 = emp()

emp1.get_name_age_salary("Jan", 33, 1000)
emp2.get_name_age_salary("Magda", 24, 3000)

emp1.display_details()
emp2.display_details()

def foo(x):
    return x ** 2
print(foo("Hello"))
