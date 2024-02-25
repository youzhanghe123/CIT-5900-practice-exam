class SystemCreator:
    '''A class for loading user credential information from a file, storing it
    in a dictionary, and creating a second dictionary that keeps track of which
    users are currently logged in.'''
    
    # We are not going to use an __init__ function. We'll just call the default
    # constructor.
    
    def init_db(self, file):
        '''
        Loads the given .csv file containing user credentials.
        Each row is a comma-separated list including username and password.

        Example(s):
        lbrandon,My_Crazy_Password_1234
        tjones,4er3yw6rt5R
        dennisq,0987poiu1234QwEr

        Stores the usernames and passwords in a users dictionary where the
        username is the key and the password is the value.

        Creates an empty logged_in dictionary for storing user log-ins where the
        username is the key and the value is a bool indicating
        if the user is logged in or not.
        '''
        users = {}
        
        # TODO insert your code
        
        logged_in = {}
        
        
        with open(file,"r") as f:
            for line in f:
                line=line.strip()
                line_lis=line.split(",")
                line_lis=[element.strip() for element in line_lis]
                username=line_lis[0]
                password=line_lis[1]
                users[username]=password
        
        return users, logged_in