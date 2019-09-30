from app import app, db


class User(db.Model):
    __tablename__ = '{prefix}{name}'.format(
        prefix=app.config['TABLE_PREFIX'],
        name='user')
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    statuses = ('active', 'inactive')
    status = db.Column(db.Enum(*statuses), nullable=False)
