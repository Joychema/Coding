#inheritance

class User():
    def __init__(self, username, email,):
        self.username = username
        self.email = email

    def login(self):
        return f"{self.username} logged in"

    def logout(self):
        return f"{self.username} logged out"

class Admin(User):
    def __init__(self,username, email,id):
        super().__init__(username, email)
        self.id = id

    def delete_user(self):
        return f"{self.id} deleted"

class Customer(User):
    def __init__(self,username,email, item):
        super().__init__(username, email)
        self.item = item

    def purchase(self):
        return f"{self.item} purchased"

# class Guest(User):
#     def __init__(self,username,email,guestId):
#         super().__init__(username, email)
#         self.guestId = guestId

user = User("John Doe", "johndoe@gmail.com")
admin =Admin("user" ,"user@gmail.com", 4356789)
customer = Customer("Mark", "mark@gmail.com", "Yoghurt")

print(user.login())
print(user.logout())
print(admin.delete_user())
print(customer.purchase())
