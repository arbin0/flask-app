from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    new_name = Name(name=name)
    db.session.add(new_name)
    db.session.commit()
    return f'Hello, {name}!'

@app.route('/api/names', methods=['GET'])
def get_names():
    names = Name.query.all()
    names_list = [{"id": name.id, "name": name.name} for name in names]
    return jsonify(names_list)

if __name__ == '__main__':
    # Create tables
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
