from flask_app.config.mysqlconnection import connectToMySQL

class User:
    
    # FROM REQUEST.FORM
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #CREATE
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return cls(result[0])

    # UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = "delete from users where id = %(id)s"
        return connectToMySQL('users_schema').query_db( query, data )