from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = 'recipes_db'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#! Staticmethods here #################################################
    #staticmethod to validate email 
    @staticmethod
    def validate_email(new_email):
        is_valid = True
        # test whether email submitted is an actual email
        if not EMAIL_REGEX.match(new_email['email']): 
            flash ("Email is not valid!")
            is_valid = False
        # test to verify the email doesn't already exist in the db
        query = """
        SELECT * 
        FROM users
        WHERE email = %(email)s;
        """    
        #in static method can use "User.DB" or 'schema name in string'
        results = connectToMySQL('recipes_db').query_db(query,new_email)
        # use to check if working...
        print(results)

        if results:
            flash("Email already exists!")
            is_valid = False

        return is_valid
    


    #static method to validate entire user (specific to register form) // NOTICE CATEGORY FILER ON FLASH MESSAGES*
    @staticmethod
    def validate_user(new_user):
        is_valid = True
        if len(new_user['first_name']) < 2:
            flash('User first name must be 2 charecters or more!', 'register')
            is_valid = False
        if len(new_user['last_name']) < 2:
            flash('User first name must be 2 charecters or more!', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(new_user['email']):
            flash('Please enter a valid email!', 'register')
            is_valid = False
        if len(new_user['password']) < 8:
            flash('Password must be 8 or more characters long!', 'register')
            is_valid = False
        if new_user['password'] != new_user['confirm_password']:
            flash('Passwords did not match!', 'register')
            is_valid = False
        
        return is_valid





#! Classmethods here #################################################
        #classmethod to save new user registration
    @classmethod
    def save(cls,data):
        query = """INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #classmethod to get one user (via id)
    @classmethod
    def get_oneById(cls,data):
        query = """
        SELECT * 
        FROM users
        WHERE id = %(id)s;
        """    

        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])


    #classmethod to get one user (via email)
    @classmethod
    def get_oneByEmail(cls,data):
        query = """
        SELECT * 
        FROM users
        WHERE email = %(email)s;
        """    
        #if it's not in the DB it will be False
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])







#! Reminder mesages here #################################################

# Have import from mysqlconnection on every model for DB interactions
# Import the model's python file as a module, not the class directly so you avoid circular import errors!
# For example: from flask_app.models import table2_model

'''
! Note: If you are working with tables that are related to each other, 
!       you'll want to import the other table's class here for when you need to create objects with that class. 

! Example: importing pets so we can make pet objects for our users that own them.

Class should match the data table exactly that's in your DB.

REMEMBER TO PARSE DATA INTO OBJECTS BEFORE SENDING TO PAGES!

'''
