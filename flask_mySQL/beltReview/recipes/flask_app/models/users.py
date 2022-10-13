from flask_app import DATABASE, bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app.models import recipes

class User:
    
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    #CREATE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(password)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query = "select * from users left join recipes on users.id = recipes.user_id where users.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(result[0])
        all_recipes = []
        for recipe in result:
            recipe_data = {
                'id': recipe['recipes.id'],
                'user_id': recipe['user_id'],
                'name': recipe['name'],
                'description': recipe['description'],
                'instructions': recipe['instructions'],
                'under_30':recipe['under_30'],
                'created_at':recipe['recipes.created_at'],
                'updated_at':recipe['recipes.updated_at']
            }
            all_recipes.append(recipes.Recipe(recipe_data))
        user.recipes = all_recipes
        return user

    # @classmethod
    # def get_one_user_name(cls, data):
    #     query = "select first_name from recipes join users on recipes.user_id = users.id where recipes.id = %(id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     print(result)
    #     if not result:
    #         return False
    #     return cls(result[0])

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    # # UPDATE
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db( query, data )
    
    # #DELETE
    # @classmethod
    # def delete(cls, data):
    #     query = "delete from users where id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def validate_new_user (user):
        is_valid = True
        # query = "SELECT * FROM users WHERE email = %(email)s;"
        # results = connectToMySQL(DATABASE).query_db(query, user)

        if len(user['first_name']) < 2 or len(user['last_name']) < 2:
            flash('name too short, get a longer name', 'reg')
            is_valid = False

        # if len(results) >= 1:
        #     flash("email already existsts please pick a new one")
        #     is_valid = False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'reg')
            is_valid = False

        if user['password'] != user['password_confirm']:
            flash('passwords do not match, try again', 'reg')
            is_valid = False

        potential_user = User.get_one_by_email({'email':user['email']})
        if potential_user:
            flash('email already exists', 'reg')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True

        if len(user['email']) < 1:
            flash('invalid email, try again', 'login')
            is_valid = False
        
        elif not EMAIL_REGEX.match(user['email']):
            flash('invalid email', 'login')
            is_valid = False

        if len(user['password']) < 8:
            flash('password too short', 'login')
            is_valid = False
        
        if is_valid:
            potential_user = User.get_one_by_email({'email':user['email']})
            if not potential_user:
                flash('email does not exist', 'login')
                is_valid = False
            else:
                if not bcrypt.check_password_hash(potential_user.password, user['password']):
                    flash('password incorrect try again', 'login')
                    is_valid = False
                else:
                    session['session_userid'] = potential_user.id
        return is_valid
