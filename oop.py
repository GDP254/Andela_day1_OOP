import unittest

class Vehicle(object):
    
    #Properties shared by all vehicles in the game 
    speed = 0
    num_of_wheels = 1 # minimum

    #Constructor
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def Sound(self):
        print ""

# Inheritance demonstration
class Motorcycle(Vehicle):

    #Properties of a motorcycle in game overriden to represent a motorcycle
    num_of_wheels = 2
    #constructor stays the same

    def Sound(self):
        return "High Pitch Sound"

class Car(Vehicle):
    #Property num_of_doors is specific to Cars in this game
    num_of_doors = 4
    num_of_wheels = 3 # minimum
    #constructor stays the same

    def Sound(self):
        return "Low Pitch Sound"

class VehicleClassTest(unittest.TestCase):

    """
        The following test cases are a demonstration of INHERITANCE
    """

    def test_car_instance(self):
        honda = Car('Honda', 'Fit')
        self.assertIsInstance(honda, Vehicle, msg='The object should be an instance of the `Vehicle` class')

    def test_motorcycle_instance(self):
        honda = Motorcycle('Honda', 'CBR 200')
        self.assertIsInstance(honda, Vehicle, msg='The object should be an instance of the `Vehicle` class')

    def test_object_type(self):
        honda = Car('Honda', 'Escudo')
        self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

    def test_object_type2(self):
        suzuki = Motorcycle('Suzuki', 'GXSR')
        self.assertTrue((type(suzuki) is Motorcycle), msg='The object should be a type of `Motorcycle`')

    """
        The following test cases are a demonstration of POLYMORPHISM
    """

    def test_car_sound(self):
        toyota = Car('Toyota', 'Prado')
        self.assertEqual('Low Pitch Sound', toyota.Sound(),
                         msg='The car should be make a low pitch sound')

    def test_motorcycle_sound(self):
        yamaha = Motorcycle('Yamaha', 'R6')
        self.assertEqual('High Pitch Sound', yamaha.Sound(),
                         msg='The motorcycle should be make a high pitch sound')

if __name__ == "__main__":
  unittest.main()