from flask import Flask

from kata_api_entreprise.view.view import bp


def create_app(config='dev'):
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)










# API_ENTREPRISE_BASE_URL = 'https://entreprise.api.gouv.fr/v2/etablissements/'
# API_ENTREPRISE_TOKEN = 'p9A9funz6VJZGy1ZWI3d6aBIMJqIpcSB'
# API_ENTREPRISE_CONTEXT = 'Demande d\'embauche d\'un salarié étranger'
# API_ENTREPRISE_OBJECT = 'Gestion Automatisée de l\'immigration professionnelle'
# SIREN_DGEF = '130017593'

# @bp.route('/entreprise/<siret>')
# def index(siret):
#     url = 'https://entreprise.api.gouv.fr/v2/etablissements/{siret}/'.format(siret=siret)
#     params = {
#         'context': API_ENTREPRISE_CONTEXT,
#         'recipient': SIREN_DGEF,
#         'object': API_ENTREPRISE_OBJECT,
#         'token': API_ENTREPRISE_TOKEN
#     }
#     response = requests.get(url, params=params)
#     return response.text

# response = self.client.get('/entreprise/41816609600069')
