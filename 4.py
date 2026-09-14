class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        if self.battery < 20:
            print(self.name, "cannot move. Battery is too low.")
        else:
            print(self.name, "is moving.")

    def charge(self):
        self.battery = 100
        print(self.name, "is fully charged.")


class DeliveryRobot(Robot):
    def move(self):
        if self.battery < 20:
            print(self.name, "cannot move. Battery is too low.")
        else:
            print(self.name, "moves to a delivery location.")


class SecurityRobot(Robot):
    def move(self):
        if self.battery < 20:
            print(self.name, "cannot move. Battery is too low.")
        else:
            print(self.name, "patrols a specific area.")


class RescueRobot(Robot):
    def move(self):
        if self.battery < 20:
            print(self.name, "cannot move. Battery is too low.")
        else:
            print(self.name, "moves toward a disaster location.")


robot1 = DeliveryRobot("Delivery Robot", 80)
robot2 = SecurityRobot("Security Robot", 50)
robot3 = RescueRobot("Rescue Robot", 15)

robot1.move()
robot2.move()
robot3.move()

robot3.charge()
robot3.move()
