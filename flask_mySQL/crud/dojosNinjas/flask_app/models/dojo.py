from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    
    # FROM REQUEST.FORM
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #CREATE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        return connectToMySQL(DATABASE).query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    # # UPDATE
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE dojos SET dojo=%(dojo)s;"
    #     return connectToMySQL(DATABASE).query_db( query, data )
    
    # #DELETE
    # @classmethod
    # def delete(cls, data):
    #     query = "delete from dojos where id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db( query, data )