class Car(object):
    condition = "new"

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def description(self):
        print "It's a %s %s very nice car!" % (self.color, self.brand)

    def drive_car(self, speed, hours):
        distence = speed * hours
        print "Driving very happy ..."
        if distence < 30000:
            self.condition = "like new"
        elif distence < 100000:
            self.condition = "second hand"
        else:
            self.condition = "too old"


my_car = Car("silver", "Benz")

my_car.description()
print "It's a", my_car.condition, "car"
my_car.drive_car(20, 2000)
print "It's a", my_car.condition, "car"
