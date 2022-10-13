from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Email:
    
    # FROM REQUEST.FORM
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO emails (email , created_at) VALUES (%(email)s , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM emails WHERE id = %(id)s"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     return cls(result[0])

    
    # #DELETE
    # @classmethod
    # def delete(cls, data):
    #     query = "delete from EMAILS where id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def valid_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,email)

        if len(email['email']) < 1:
            flash('enter an email')
            is_valid=False
        
        if len(results) >= 1:
            flash("email taken")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("invalid email")
            is_valid=False
        return is_valid