
class Gun:
    def __init__(self, name="", bulletNum=0):
        self.name = name
        self.bulletNum = bulletNum

    def shoot(self):
        if self.bulletNum > 0:
            self.bulletNum -= 1;
            print("Gun:%s 打出一颗子弹" % self.name)
            return True
        else:
            print("子弹不足")
            return False

    def addNewBullet(self, num=0):
        self.bulletNum += num
        print("Gun:%s 添加子弹%d颗" % (self.name, num))

    def __str__(self):
        return ("Gun: \r\n  name->%s  \r\n bulletNum->%d"
                % self.name, self.bulletNum)

class Soldier:

    def __init__(self, name="", gun=None):
        self.name = name
        self.gun  = gun

        # 私有属性 外部无法访问  如果想访问可以使用 _类名+属性名 self._Soldier__secretOption
        self.__secretOption = "secretOption"

    # 私有方法 外部无法访问 如果想访问可以使用 _类名+方法名 self._Soldier__secretFun()
    def __secretFun(self):
        print(" 这是一个私有方法 ")

    def fire(self):
        # is 判断连个变量引用的对象是否为同一个 类似于I id(a) == id(b)
        # == 判断两个变量的值是否为同一个
        if self.gun is None:
            print("没枪，开个毛线火")
            return

        if self.gun.bulletNum == 0:
            self.gun.addNewBullet(10)
            self.gun.shoot()
        else:
            self.gun.shoot()

    def getGun(self, gun=None):
        self.gun = gun

    def __str__(self):
        return ("Soldier: \r\n   name->%s \r\n   gun:%s"
                % self.name, self.gun)



AK47 = Gun("AK47", 2)

xuSanDuo = Soldier(name="xuSanDuo")
xuSanDuo.fire()
xuSanDuo.getGun(AK47)
xuSanDuo.fire()
xuSanDuo.fire()
xuSanDuo.fire()

# 间接访问私有内容  不推荐使用
print(xuSanDuo._Soldier__secretOption)
xuSanDuo._Soldier__secretFun()
