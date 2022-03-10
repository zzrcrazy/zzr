class BenzCar:
    brand = '奔驰'
    country = '德国'
    price = 338800

    @staticmethod
    def pressHorn():
        print('嘟嘟----')

    def __init__(self, color, brand):
        self.brand = brand
        self.color = color


car1 = BenzCar('蓝色','葫芦娃')
car2 = BenzCar('','')
print(car1.brand)
print(car1.color)





