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


    def delete_credentials(self):
        '''
        Method that deletes a saved contact from the list .
        '''
        Contact.contact_list.remove(self)

    @classmethod
    def display_credentials(cls,name):
        '''
        method that returns a list of credentials_list
        '''
        for credentials in cls.credentials_list:
            if credentials.account_username == name :
                return cls.credentials_list
