class User():
    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.login_attempts = 0
    
    def describe_user(self):
        '''
        This function prints summary of the user's information.
        It takes no argument.
        '''
        print(f"First Name:\t{self.first_name}")
        print(f"Last Name:\t{self.last_name}")
        print(f"Age:\t\t{self.age}")
        print(f"Address:\t{self.address}")
        
    def greet_user(self):
        '''
        This function greets the user. It takes no argument.
        '''
        print((f"Hello {self.first_name} {self.last_name}, I hope"
                " you are doing well!"))
        
    def increment_login_attempts(self):
        '''
        This function increments login_attempts by 1. It takes no argument.
        '''
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        '''
        This function resets the login_attempts. It takes no argument.
        '''
        self.login_attempts = 0
        
class Admin(User):
    def __init__(self, privileges):
        self.privileges = Privileges(privileges)
        
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        '''
        This function just show the list of privileges an admin have.
        It takes no argument.
        '''
        print("Admin have following privileges")
        for privilege in self.privileges:
            print(privilege)