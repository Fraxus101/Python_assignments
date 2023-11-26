from flask_app.config.mysqlconnection import connectToMySQL, DB

class user:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#1 select all
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        friends=[]
        for row in results:
            friend = cls(row)
            friends.append(friend)
        return friends

#2 select by id
    @classmethod
    def select_friend(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data)
        friend = None
        if results != []:
            friend = cls(results[0])
        return friend

#3 Create 
    @classmethod
    def create_friend(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL(DB).query_db(query, data)
        return results