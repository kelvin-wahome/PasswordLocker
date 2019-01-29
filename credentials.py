class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list =[]

    def __init__(self,account,name,password):
        self.account_name = account
        self.account_username = name
        self.account_password = password
