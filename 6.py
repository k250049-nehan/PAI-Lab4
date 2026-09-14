class Computer:
    def __init__(self, cpu, ram, battery):
        self.cpu = cpu
        self.ram = ram
        self.battery = battery

    def system_status(self):
        print("CPU:", self.cpu, "%")
        print("RAM:", self.ram, "%")
        print("Battery:", self.battery, "%")

        if self.cpu > 80:
            print("Heavy CPU Load")

        if self.ram > 85:
            print("High Memory Usage")

        if self.battery < 20:
            print("Low Battery")


computer1 = Computer(90, 70, 15)
computer2 = Computer(50, 90, 60)

print("Computer 1")
computer1.system_status()

print()

print("Computer 2")
computer2.system_status()
