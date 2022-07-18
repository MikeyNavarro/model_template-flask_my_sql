# pipenv install flask pymysql flash black 
from flask_app.controllers import dojos , ninjas
# From flask app Import specific controllers 
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)
