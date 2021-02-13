from user import User

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