class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, password):
        if password not in self.old_passwords:
            self.old_passwords.append(password)

    def is_correct(self, password):
        return password == self.get_password()


if __name__ == "__main__":
    pass