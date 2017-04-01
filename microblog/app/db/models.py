from microblog.app import db_object

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db_object.Model):
    id = db_object.Column(db_object.Integer, primary_key=True)
    nickname = db_object.Column(db_object.String(64), index=True, unique=True)
    email = db_object.Column(db_object.String(120), index=True, unique=True)
    role = db_object.Column(db_object.SmallInteger, default=ROLE_USER)
    posts = db_object.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db_object.Model):
    id = db_object.Column(db_object.Integer, primary_key=True)
    body = db_object.Column(db_object.String(140))
    timestamp = db_object.Column(db_object.DateTime)
    user_id = db_object.Column(db_object.Integer,
                               db_object.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
