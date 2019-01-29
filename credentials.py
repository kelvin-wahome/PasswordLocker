class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list =[]

    def __init__(self,account,name,password):
        self.account_name = account
        self.account_username = name
        self.account_password = password

    def save_credentials(self):
        '''
        Method to save credentials object into credentials_list
        '''
        Credentials.credentials_list.append(self)
