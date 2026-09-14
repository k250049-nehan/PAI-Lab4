class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        print("Agent is performing a task")


class SecurityAgent(Agent):
    def perform_task(self):
        print(self.name, "is detecting cyber threats.")


class MonitoringAgent(Agent):
    def perform_task(self):
        print(self.name, "is monitoring system activity.")


class RecoveryAgent(Agent):
    def perform_task(self):
        print(self.name, "is recovering system services.")


agent1 = SecurityAgent("Security Agent", "Active")
agent2 = MonitoringAgent("Monitoring Agent", "Active")
agent3 = RecoveryAgent("Recovery Agent", "Active")

agent1.perform_task()
agent2.perform_task()
agent3.perform_task()
