from app import app, db


class Role(db.Model):
    __tablename__ = '{prefix}{name}'.format(
        prefix=app.config['TABLE_PREFIX'],
        name='role')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
