class person:
    def __init__(self,color, age, name):
        self.color = color
        self.age = age
        self.name = name
    def get(self):
        return ( " {} {} {} " .format(self.color,self.age,self.name))

a = person("red", 2,"japan")
print(a.get())

class student(person):
    def __init__(self, color, age, name, en):
        super().__init__(color, age,name)
        self.en = en
    def print(self):
        return "{} {} {} {}".format(self.color, self.age, self.name, self.en)

b = student("blue", 3,"karan",134)
print(b.get())

class junior(student):
    def __init__(self, color, age, name, en,std):
        super().__init__(color, age,name,en)
        self.std = std
    def print(self):
        return "{} {} {} {} {}".format(self.color, self.age, self.name, self.en, self.std )

d = junior("orange", 5, "japan",134,"3rd")
print(d.print())