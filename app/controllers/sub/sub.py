from flask import Blueprint

sub_blueprint = Blueprint(
    'sub',
    __name__,
    url_prefix="/sub"
)


@sub_blueprint.route('/', methods=['GET'])
def index():
    return 'sub'


@sub_blueprint.route('/new', methods=['GET'])
def new():
    return 'new sub!'
