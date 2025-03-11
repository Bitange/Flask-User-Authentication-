from flask import Flask, render_template,redirect ,request,session,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os


app= Flask(__name__)

#config sql alchemy
app.config["SQLALCHEMY_DATABASE_URI"]= os.environ.get("DATABASE_URI","postgresql://postgres:1234@localhost:5432/flask_auth_db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)



#database model


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  
    



#routes
@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template ("index.html")






if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)