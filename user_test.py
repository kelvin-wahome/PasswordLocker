import unittest # Importing the unittest module
from user import User # import user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''

    def tearDown(self):
            '''
            tearDown method that does cleanup after each test case has run
            '''
            User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases .
        '''
        self.new_user = User("Kelvin Wahome","callofduty")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Kelvin Wahome")
        self.assertEqual(self.new_user.user_password,"callofduty")
        self.assertEqual(self.new_credentials.account_name,"Instagram")
        self.assertEqual(self.new_credentials.account_username,"Kelvin Wahome")
        self.assertEqual(self.new_credentials.account_password,"callofduty")

    def test_save_user(self):
        '''
        test case to test if the user object is saved
        '''
        self.new_user.save_user() # save a user
        self.assertEqual(len(User.user_list),1)

    def test_multiple_user(self):
        '''
        test case to check if we can save multiple user objects
        '''
        self.new_user.save_user()
        test_user = User("Test","kenya")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    @classmethod
    def display_credentials(cls,name,password):
        '''
        test case to test if we can display credentials by name and password
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



if __name__ == '__main__':
    unittest.main()
