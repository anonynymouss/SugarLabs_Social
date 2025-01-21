from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///software.db'
app.config['SECRET_KEY'] = 'your-secret-key'

db = SQLAlchemy(app)
admin = Admin(app, name='Software Admin', template_mode='bootstrap3')

# Define your model
class Software(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)

# Add the model to the admin
admin.add_view(ModelView(Software, db.session))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
