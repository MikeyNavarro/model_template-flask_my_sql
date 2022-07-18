from flask_app.config.mysqlconnection import connectToMySQL
# This import connects to MySQL and returns a database connection
from flask_app.models import dojo

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']