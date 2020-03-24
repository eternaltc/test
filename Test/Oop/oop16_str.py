class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "名字是{0}".format(self.name)

P = Person("tc")
print(P)

