class Employee:
    def __init__(self, name, org,):
        self.name = name
        self.org = org

    def show(self):
        print(f"Good Evening! My name is {self.name} and I work at {self.org}.")

emp = Employee('Shreyas', 'Accenture')

emp.show()