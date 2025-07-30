class vehicle:
    def start_engine(self):
        print("Engine started....")
class car(vehicle):
    def drive(self):
        print("The car is being drove")
c=car()
c.start_engine()#inherited method
c.drive() #sub class own methoid
