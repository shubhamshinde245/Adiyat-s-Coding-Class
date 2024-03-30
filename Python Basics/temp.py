login = []
password = []


def register():
    print("Register")
    login.append(input("Enter login: "))
    password.append(input("Enter password: "))
    print("You have successfully registered")


register()
print("Users", login)
print("Password", password)
