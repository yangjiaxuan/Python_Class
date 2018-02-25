
class Cat:
    # 这是一个初始化方法 用类名()时，会自动调用初始化方法
    def __init__(self, name=""):
        print("cat 初始化")
        # 在初始中添加一个属性，这样后面所有的对象中就都有这个属性了，并拥有初始值
        self.name = name

    # 析构方法
    def __del__(self):
        print("cat %s 被销毁了" % self.name)


    def __str__(self):
        return "Cat: name->%s" % self.name

    # 这是一个猫类
    def eat(self):
        print("cat:%s 吃鱼" % self.name)
    def drink(self):
        print("cat:%s 喝水" % self.name)

def printCatInfo(cat):
    # 打印对象 默认打印__str__ 返回的字符串，如果不重写__str__方法，则打印默认内容
    print(cat)
    addr = id(cat)
    # 打印对象地址
    print("%s addr:%d" % (cat.name, addr))

tom = Cat()
# 不修改类直接给对象添加属性, 如果一个类中没有定义属性，调用时就会报错
tom.name = "Tom"
tom.eat()
tom.drink()
printCatInfo(tom)

# del: 销毁对象  使对象提前调用__del__方法，销毁对象
del tom

lazy_cat = Cat("LazyCat")
lazy_cat.eat()
lazy_cat.drink()
printCatInfo(lazy_cat)
