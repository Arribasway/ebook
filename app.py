from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ebook.db"
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(255),nullable=False)


@app.route("/")     
def home():
    return  render_template("index.html")

@app.route("/register")
def register():
  if request.method == "POST":
     print(request.form)
     return ""
  else:
    return  render_template("register.html")

@app.route("/login")
def login():
  return  render_template("login.html")

def create_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    #create_db()
    app.run(debug=True)