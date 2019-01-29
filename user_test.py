import unittest # Importing the unittest module
from user import User # import user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''
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

    def test_save_user(self):
        '''
        test case to test if the user object is saved
        '''
        self.new_user.save_user() # save a user
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
