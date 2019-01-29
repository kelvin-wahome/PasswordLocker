#!/usr/bin/env python3.6
from user  import User
from credentials import Credentials

    def create_user(name,password):
        '''
        Function to create a new user
        '''
        new_user = User(name,password)
        return new_user


    def save_user(user):
        '''
        Function to save user
        '''
        user.save_user()

    def del_credentials(credentials):
        '''
        Function to delete credentials
        '''
        credentials.delete_credentials()
