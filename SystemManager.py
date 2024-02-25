class SystemManager:
    '''A class for managing system operations.
    '''
    
    # We are not going to use an __init__ function. We'll just call the default
    # constructor.
    
    def check_username_password(self, users, username, password):
        '''
        Checks whether the username exists in the users dictionary and that the password matches the username.  Returns boolean.
        '''
        
        # TODO insert your code
        return (username in list(users.keys())) and (users[username]==password)
    
    def is_valid_password(self, password):
        '''
        Checks whether the given password is valid.  Returns boolean.
        The length of a valid password should be at least 8 characters and it should contain
        at least one lowercase character, one uppercase character, and one number.
        '''
        
        # TODO insert your code
        lower= False
        upper=False
        number=False
        for char in password:
            if char.islower():
                lower=True
            elif char.isupper():
                upper=True
            elif char.isnumeric():
                number=True
            
        return len(password)>=8 and lower and upper and number
    
    def sign_up(self, users, logged_in, username, password):
        '''
        Allows users to sign up.
        If the username already exists in the users dictionary, prints a friendly message.
        If the password does not satisfy the rule(s) (not valid), prints a friendly message.
        Otherwise, saves the username and the corresponding password in the users dictionary, and prints a
        success message.

        Note(s):
        The user is not automatically logged in when he/she signs up.
        '''
        
        # TODO insert your code
        if username in list(users.keys()):
            logged_in[username]=False
            print("The user has already exists")
        elif not(self.is_valid_password( password)):
            print('The password does not satisfy the rules')
        else:
            users[username]=password
            logged_in[username]=False
        return 
            
    
    def log_in(self, users, logged_in, username, password):
        '''
        Allows users to log in.
        If the username does not exist in the users dictionary or the password is incorrect, prints an error message.
        Otherwise, saves the username and the value of True in the logged_in dictionary, and prints a welcome message.

        Note(s):
        Even if a user is already logged in, he/she can log in again.
        '''
        # TODO insert your code
        if not(self.check_username_password(users, username, password)):
            print('There is an error')
        else:
            logged_in[username]=True
            print("Welcome!")
        return
        
    
    def change_password(self, users, username, old_password, new_password):
        '''
        Allows users to change their password.
        If the username does not exist in the users dictionary, prints an error message.
        If the old_password is incorrect, prints an error message.
        If the new_password does not satisfy the rule(s) (not valid), prints an error message.
        Otherwise, changes the user's password in the users database, and prints a success message.
        '''
        # TODO insert your code
        
        if not self.check_username_password(users, username, old_password):
            print('The user does not exists or the old password is incorrect')
        else:
            if not(self.is_valid_password(new_password)):
                print("The new password is invalid")
            else :
                users[username]=new_password
                print("The user has successfully changed the password!")
    
    def delete_account(self, users, logged_in, username, password):
        '''
        Allows users to delete their account.
        If the username does not exist in the users database, prints an error message.
        If the old_password is incorrect, prints an error message.
        Otherwise, deletes the user's account from the users dictionary, and prints a success message.

        Note(s):
        Also deletes the user's information in the logged_in dictionary.
        '''

        # TODO insert your code
        if not self.check_username_password(users, username, password):
            print('The user does not exists or the old password is incorrect')
        else:
            print("debug ", )
            users.pop(username)
            if username in list(logged_in.keys()):
                logged_in.pop(username)
            print("The user has successfully deleted the account!")
        
    
    def get_sign_ups(self, users):
        '''
        Returns a list of users who are signed up (in the users dictionary).
        '''
        
        # TODO insert your code
        return list(users.keys())
    
    def get_log_ins(self, logged_in):
        '''
        Returns a list of users who are logged in (in the logged_in dictionary).
        '''

        # TODO insert your code
        return list(logged_in.keys())
    
    