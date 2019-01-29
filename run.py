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


    def main():
        print("PASSWORD LOCKER")
        print("Hi welcome to password locker. What's your name?")
            user_name = input()
            print('\n')
            while True:
               print(f"Wassup {user_name}!!.Use these short codes: cu-create new user, cc-create new credentials,")

               short_code = input().lower()
               if short_code == 'cu':
                   print("Sign Up")

                   print("User name ...")
                   u_name = input()
                   print("Password ...")
                   u_password = input()

                   save_user(create_user(u_name,u_password)) #create and save user
                   print('\n')
                   print(f"New User {u_name} created!")
                   print('\n')

               elif short_code == 'cc':
                   print ("Add new credentials")

                   print("User name .. ")
                   u_name = input()
                   print("Account name .. ")
                   a_name = input()
                   print("Password ..")
                   password = input()

                   save_credentials(create_credentials(u_name,a_name,password))
                   print('\n')
