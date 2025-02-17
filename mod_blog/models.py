from app import db
class Post (db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True,unique=True)
    title=db.Column(db.String(256))
    summary=db.column(db.String(256))
    content=db.Column(db.Text)
    slug=db.Column(db.String(256))
class Category(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=True,unique=True)
    name=db.Column(db.String(256))
    description=db.Column(db.String(256))
    slug=db.Column(db.String(256))  
    posts = db.relationship('Post', secondary='category_post', backref=db.backref('categories', lazy='dynamic'))

category_post = db.Table('category_post',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
                         )      
