class Dog:
    def __init__(self, name, color, age, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed

    def show(self):
        print(f"Hello! My name is {self.name} and I am a {self.age} years old {self.color} {self.breed}.")

pet1 = Dog('Tommy', 'Black', 3, "labrador")
pet2 = Dog('Jax', 'White', 2, 'Shih Tzu')
pet3 = Dog('Bailey','', 4, 'Golden Retriver')

pet1.show()
pet2.show()
pet3.show()