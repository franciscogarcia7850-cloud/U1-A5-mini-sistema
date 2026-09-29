from flask import Flask
from flask_wtf.csrf import CSRFProtect

from bd import db, URI
from routes.users import users_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'francisco'
app.config['SQLALCHEMY_DATABASE_URI'] = URI

db.init_app(app)
CSRFProtect(app)
app.register_blueprint(users_bp)

# Crea la tabla users si todavía no existe
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
