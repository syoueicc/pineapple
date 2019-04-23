import os
from flask_migrate import Migrate
from werkzeug.contrib.fixers import ProxyFix
from app import create_app
from app.models import db, User, Post
from app.schemas import UserSchema

env = os.getenv('PACAT_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, UserSchema=UserSchema)


@app.cli.command('test')
def test_command():
    print("test command shot...")


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'])
