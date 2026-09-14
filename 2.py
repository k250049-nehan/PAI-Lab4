class PasswordVault:
    def __init__(self, username, password):
        self.username = username
        self._vault_status = "Active"
        self.__password = password

    def change_password(self, new_password):
        self.__password = new_password
        print("Password changed successfully")

    def verify_password(self, entered_password):
        if entered_password == self.__password:
            print("Access Granted")
        else:
            print("Access Denied")

    def display_status(self):
        print("Username:", self.username)
        print("Vault Status:", self._vault_status)


user1 = PasswordVault("Nehan", "12345")

user1.display_status()

user1.verify_password("12345")
user1.verify_password("99999")

user1.change_password("abc123")
user1.verify_password("abc123")
