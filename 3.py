class SecuritySystem:
    def respond(self):
        print("Security system responding")


class Firewall(SecuritySystem):
    def respond(self):
        print("Block suspicious network traffic")


class Antivirus(SecuritySystem):
    def respond(self):
        print("Isolate malicious files")


class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Generate security alert")


firewall = Firewall()
antivirus = Antivirus()
ids = IntrusionDetectionSystem()

firewall.respond()
antivirus.respond()
ids.respond()
