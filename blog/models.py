from mongoengine import Document, StringField, DateTimeField, IntField
import datetime

class BlogPost(Document):
    title = StringField(max_length=200, required=True)
    content = StringField(required=True)
    image = StringField() 
    pub_date = DateTimeField(default=datetime.datetime.now)
    view_count = IntField(default=0)
    
    meta = {
        'collection': 'blog_posts',
        'ordering': ['-pub_date']
    }

class AdminUser(Document):
    username = StringField(max_length=150, required=True, unique=True)
    password = StringField(required=True) 
    is_staff = StringField(default="True")
    
    meta = {
        'collection': 'admin_users'
    }
