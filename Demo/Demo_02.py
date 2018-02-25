

class Person:

    def __init__(self, name="", wight=0.0):
        self.name = name
        self.wight = wight

    def __str__(self):
        return "Persion:\r\n  name->%s \r\n  wight->%.2f " % (self.name, self.wight)

    def run(self):
        self.wight -= 0.5

    def eat(self):
        self.wight = 1



xiaoMing = Person("小明", 80.0)
print(xiaoMing)

xiaoMing.eat()
print(xiaoMing)

xiaoMing.run()
print(xiaoMing)