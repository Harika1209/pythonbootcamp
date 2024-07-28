class mother:
    def mother_speak():
        return "mother is speaking"
class father:
    def father_speak():
        return "father is speaking"
class kid(mother,father):
    def kid_speak():
        return "i'm kid i have properties of class mother and father"
obj1=kid
print(obj1.mother_speak())
print(obj1.father_speak())
print(obj1.kid_speak())
    