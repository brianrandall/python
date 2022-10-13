from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    
    # FROM REQUEST.FORM
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #CREATE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojo_id) VALUES ( %(first_name)s , %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_one_dojo_id(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        ninjas = []
        for ninja in result:
            ninjas.append( cls(ninja) )
        return ninjas

    # # UPDATE
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db( query, data )
    
    # #DELETE
    # @classmethod
    # def delete(cls, data):
    #     query = "delete from ninjas where id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db( query, data )