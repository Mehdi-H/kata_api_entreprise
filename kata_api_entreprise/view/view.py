from flask import Blueprint

bp = Blueprint('myapp', __name__)


@bp.route('/entreprise')
def index():
    return 'Hello World !'
