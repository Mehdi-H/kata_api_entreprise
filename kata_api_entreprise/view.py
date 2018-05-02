from flask import Flask, Blueprint

bp = Blueprint('myapp', __name__)


@bp.route('/')
def index():
    return 'Hello, World!'


def create_app(config='dev'):
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
