from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app.models import users


class Band:
    
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.genre = data['genre']
        self.home_town = data['home_town']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #CREATE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO bands ( name, genre, home_town, created_at, updated_at, user_id ) VALUES ( %(name)s , %(genre)s , %(home_town)s, NOW() , NOW(), %(user_id)s );"
        print(data)
        return connectToMySQL(DATABASE).query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "select * from bands left join users on bands.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        
        if not results:
            return [] 
        bands = []
        for x in results:
            band_instance = cls(x)
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
            band_instance.user = user_instance
            bands.append(band_instance)

        return bands

    @classmethod
    def get_one(cls, data):
        query = "select * from bands left join users on users.id = bands.user_id where bands.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        band = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password':result[0]['password'],
            'created_at':result[0]['users.created_at'],
            'updated_at':result[0]['users.updated_at']
        }
        band.user = users.User(user_data)
        return band

    # UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE bands SET name=%(name)s, genre=%(genre)s, home_town=%(home_town)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = "delete from bands where id = %(id)s"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def validate_band (band):
        is_valid = True
        if (len(band['name']) or len(band['genre']) or len(band['home_town'])) < 3:
            flash('name, genre, and home town are required and must be at least 3 chars', 'validate_band')
            is_valid = False

        return is_valid