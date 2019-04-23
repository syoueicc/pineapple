from flask_marshmallow import Marshmallow
from app.models import User, Post

ma = Marshmallow()


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    posts = ma.Nested('PostSchema', many=True)

