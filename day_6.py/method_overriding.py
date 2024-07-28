class animal:
    def speak():
        return "hello"
class dog(animal):
    def speak():
        return "world"
class puppy(dog):
    def speak():
        return "hello world"
obj1=puppy
print(obj1.speak())