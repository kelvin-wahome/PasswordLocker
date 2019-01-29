class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty contact list

    def __init__(self,name,password):

      # docstring removed for simplicity

        self.first_name = name
        self.user_password = password
