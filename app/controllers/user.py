from flask import Blueprint, jsonify
from sqlalchemy.sql import expression

from app.models import User, db
from app.schemas import UserSchema

user_blueprint = Blueprint(
    'user',
    __name__,
    url_prefix="/user"
)


@user_blueprint.route('/', methods=['GET'])
def users():
    user_all = User.query.all()
    user_schema = UserSchema()
    result = user_schema.dump(user_all, many=True, update_fields=False).data
    return jsonify(result)


@user_blueprint.route('/new/<name>/<pwd>', methods=['GET'])
def create_user(name, pwd):
    new_user = User(username=name, password=pwd)
    try:
        db.session.add(new_user)
        db.session.commit()
    except expression as identifier:
        print(identifier)
        return jsonify({
            'code': 10086,
            'message': 'error'
        })
    
    return jsonify({
      'code': 0,
      'message': 'success'
    })
