class Animal:
    def speak():
        return "animal is speaking"
    # single inh:
class dog(Animal):
    def bark():
     return "bow.."
# class puppy()
obj1=dog
print(obj1.bark())
print(obj1.speak())

