class CyberAgent:
    def __init__(self, name, status, threat_score):
        self.name = name
        self.status = status
        self.__threat_score = threat_score

    def update_threat_score(self, score):
        self.__threat_score = score

    def get_threat_score(self):
        return self.__threat_score

    def analyze(self):
        print(self.name, "is analyzing.")

    def respond(self):
        print(self.name, "is responding.")


class NetworkAgent(CyberAgent):
    def analyze(self):
        print(self.name, "is analyzing network traffic.")

    def respond(self):
        print(self.name, "is blocking suspicious network activity.")


class MalwareAgent(CyberAgent):
    def analyze(self):
        print(self.name, "is analyzing malicious files.")

    def respond(self):
        print(self.name, "is isolating the malware.")


class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        print(self.name, "is analyzing the security incident.")

    def respond(self):
        print(self.name, "is recovering the affected system.")


agent1 = NetworkAgent("Network Agent", "Active", 40)
agent2 = MalwareAgent("Malware Agent", "Active", 80)
agent3 = IncidentResponseAgent("Incident Response Agent", "Active", 90)

agent1.analyze()
agent1.respond()
print("Threat Score:", agent1.get_threat_score())

print()

agent2.analyze()
agent2.respond()
print("Threat Score:", agent2.get_threat_score())

print()

agent3.analyze()
agent3.respond()
print("Threat Score:", agent3.get_threat_score())

agent1.update_threat_score(70)
print()
print("Updated Threat Score:", agent1.get_threat_score())
