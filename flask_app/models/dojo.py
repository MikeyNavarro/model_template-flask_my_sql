from flask_app.config.mysqlconnection import connectToMySQL
# This import connects to MySQL and returns a database connection
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']