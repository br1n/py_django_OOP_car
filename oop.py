class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Max Speed: " + str(self.max_speed) + "MPH"
        print "Miles: " + str(self.miles)
        return self 

    def ride(self):
        self.miles += 10
        return self 

    def reverse(self):
        self.miles -= 5
        #bike can't go negative miles - if statement sets
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(150, 21)
bike2 = Bike(300, 32)
bike3 = Bike(700, 41)

print bike1.ride().ride().ride().reverse().displayInfo()
print bike2.ride().ride().reverse().reverse().displayInfo()
print bike3.reverse().reverse().reverse().displayInfo()

#all methods can return self to chain besides __init__ 

