from flask import Blueprint

subclass_blueprint = Blueprint(
    'subclass',
    __name__,
    url_prefix="/sub/subclass"
)


@subclass_blueprint.route('/', methods=['GET'])
def index():
    return 'subclass'


@subclass_blueprint.route('/new', methods=['GET'])
def new():
    return 'new subclass!'
