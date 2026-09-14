class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level

    def scan(self):
        print("Device:", self.device_name)
        print("IP Address:", self.ip_address)

        if self.threat_level == "Low":
            print("System Safe")
        elif self.threat_level == "Medium":
            print("Suspicious Activity")
        elif self.threat_level == "High":
            print("Critical Threat Detected")
        else:
            print("Invalid Threat Level")


device1 = ThreatDetector("PC-01", "192.168.1.10", "Low")
device2 = ThreatDetector("Server-01", "192.168.1.20", "High")

device1.scan()
print()
device2.scan()
