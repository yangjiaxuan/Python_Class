
class HouseItem:
    def __init__(self, area=0, name=""):
        self.area = area
        self.name = name

    def __str__(self):
        return ("HouseItem:\r\n   area->%.2f \r\n   name->%s" %
                (self.area, self.name))

class House:

    def __init__(self, house_type="", area=0, item_list=[]):
        self.house_type = house_type
        self.area       = area
        self.free_area  = 0
        self.item_list  = item_list
        self.calcArea()

    def addItem(self, item):
        if self.free_area < item.area:
            return False
        else:
            self.item_list.append(item)
            self.calcArea()
            return True

    def deleteItem(self, item):
        self.item_list.remove(item)
        self.calcArea()

    # 计算面积
    def calcArea(self):
        areaP = 0
        for item in self.item_list:
            areaP += item.area
        self.free_area = self.area - areaP

    def __str__(self):
        for item in self.item_list:
            print(item)
        return ("House:\r\n   type->%s \r\n   area->%.2f \r\n   free_area->%.2f \r\n" %
                (self.house_type, self.area, self.free_area))

houseA = House(house_type="A" ,area=80)

desk = HouseItem(area=2, name="desk")
houseA.addItem(desk)
print(houseA)

chair = HouseItem(area=1, name="chair")
houseA.addItem(chair)
print(houseA)

houseA.deleteItem(desk)
print(houseA)



