class UserOperations:
    usernames = []
    passwords = []

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    
    def login(self):
        if self.username in UserOperations.usernames:
            print("Valid Username !")

            if self.passwords in UserOperations.passwords:
                print("\n Login Successful !")

    def signup(self):
        u = "".join(self.username)
        p = "".join(self.password)
        print("Username :",u)
        print("Password :", p)

        UserOperations.usernames.append(u)
        UserOperations.passwords.append(p)

user = []  # Initialize an empty list

i = 0
while i >= 0:
    
    username = input("Enter Username for {} user:".format(i+1))
    # exit from the loop when the username is exit
    if username=='exit':
        break

    password = input("Enter Password for {} user:".format(i+1))

    user.append(UserOperations(username, password))  # Append a new UserOperations object to the "user" list
    user[i].signup()  # Call the signup method on the newly created UserOperations object

    i+=1

print(UserOperations.usernames)
print(UserOperations.passwords)