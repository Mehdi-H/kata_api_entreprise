import requests
from flask import Flask, Blueprint

bp = Blueprint('myapp', __name__)

API_ENTREPRISE_BASE_URL = 'https://entreprise.api.gouv.fr/v2/etablissements/'
API_ENTREPRISE_TOKEN = 'p9A9funz6VJZGy1ZWI3d6aBIMJqIpcSB'
API_ENTREPRISE_CONTEXT = 'Demande d\'embauche d\'un salarié étranger'
API_ENTREPRISE_OBJECT = 'Gestion Automatisée de l\'immigration professionnelle'
SIREN_DGEF = '130017593'


@bp.route('/entreprise/<siret>')
def index(siret):
    url = '{base_url}{siret}'.format(
        base_url=API_ENTREPRISE_BASE_URL,
        siret=siret
    )
    params = {
        'context': API_ENTREPRISE_CONTEXT,
        'recipient': SIREN_DGEF,
        'object': API_ENTREPRISE_OBJECT,
        'token': API_ENTREPRISE_TOKEN
    }
    response = requests.get(url, params=params)
    return response.text


def create_app(config='dev'):
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
