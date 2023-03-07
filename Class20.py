# Class ,object ,constructor,functions,self ,class variable,instance variable
# ,magic method/inbuilt method ,instance methods, class methods,static methods

# class methods , static methods

# instance methods => methods which are going to access with object
# class methods => methods which are going to access without object, but it can access class members
# static methods => methods which are going to access without object , but it can't access anything inside class

class car:
    brand_name = "Maruthi"

    def __init__(self, name):
        self.car_name = name
        print("I am in car class constructor")

    def engine_details(self):
        print("1000cc engine ,diesel car")
        self.body_details()

    # instance method
    def body_details(self):
        print("car body details")

    @classmethod
    def car_steering_detils(cls):
        print("Steering details")

    # class method which is accessing class variables
    @classmethod
    def tyres_details(cls):
        print("16 inch tyres")
        print("accesing class variable :", cls.brand_name)
        cls.car_steering_detils()

    # static method
    @staticmethod
    def car_seats(fabric):
        print("car seats from static method :", fabric)


obj_car = car("Baleno")
obj_car.engine_details()  # instance method , which is accessing with object
car.tyres_details()  # class method , which is accessing without object
car.car_seats("leather")  # static method ,which is accessing without object
