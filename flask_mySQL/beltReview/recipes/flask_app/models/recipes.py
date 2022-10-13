from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app.models import users


class Recipe:
    
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #CREATE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO recipes ( name, description, instructions, under_30, created_at, updated_at, user_id ) VALUES ( %(recipe_name)s , %(recipe_description)s , %(recipe_instructions)s, %(recipe_under_30)s , NOW() , NOW(), %(user_id)s );"
        print(data)
        return connectToMySQL(DATABASE).query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "select * from recipes left join users on recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return [] 
        recipes = []
        for x in results:
            recipe_instance = cls(x)
            user_data = {
                'id': x['users.id'],
                'created_at':x['users.created_at'],
                'updated_at':x['users.updated_at'],
                'first_name':x['first_name'], 
                'last_name':x['last_name'],
                'email':x['email'],
                'password':x['password']
                }
            user_instance = users.User(user_data)
            recipe_instance.user = user_instance
            recipes.append(recipe_instance)

        return recipes

    @classmethod
    def get_one(cls, data):
        query = "select * from recipes left join users on users.id = recipes.user_id where recipes.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        recipe = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password':result[0]['password'],
            'created_at':result[0]['users.created_at'],
            'updated_at':result[0]['users.updated_at']
        }
        recipe.user = users.User(user_data)
        return recipe

    # UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(recipe_name)s, description=%(recipe_description)s, instructions=%(recipe_instructions)s, under_30=%(recipe_under_30)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = "delete from recipes where id = %(id)s"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def validate_recipe (recipe):
        is_valid = True
        if (len(recipe['recipe_name']) or len(recipe['recipe_description']) or len(recipe['recipe_instructions'])) < 3:
            flash('name, description, and insctuctions are required and must be at least 3 chars', 'validate_recipe')
            is_valid = False

        return is_valid