# A fundamental concept in OOPs where a class can inherits the attributes and methods of another class.
#single inheritance
#this car class is a blueprint of the object car
#parent class
class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def drive(self):
        print(f'A person can drive {self.enginetype} car.')

#child class 
class tesla(Car):
    def __init__(self, windows, doors, engintype, is_driving):
        super().__init__(windows, doors, engintype)                             
        self.is_driving = is_driving

    def isdriving(self):
        print(f'Tesla supports self driving cars: {self.is_driving}')

# tesla1 = tesla(4,4,"electric", True)
# print(tesla1.is_driving)
# tesla1.drive()

# car1 = Car(4, 4, "electric")
# print(car1.enginetype)
# Car.drive(car1)



#Multiple inheritance 
# many parent classes and one chils class 
#parent class 1
class animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print('A sunclass must apply this method')

#parent class 2
class pet:
    def __init__(self,owner):
        self.owner=owner

    def region(self,city):
        self.city=city


#child class 

class dog(animal, pet):
    def __init__(self, name, owner):
        animal.__init__(self.name)
        pet.__init__(self.owner)

        def speak1(self):
            print(f'{self.name} says woof')

dog1 = dog("wolly",'janhvi')
# print(dog.speak1)

print(dog1.owner)
        