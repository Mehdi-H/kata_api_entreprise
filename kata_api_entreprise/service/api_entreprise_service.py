import requests

API_ENTREPRISE_BASE_URL = 'https://entreprise.api.gouv.fr/v2/etablissements/'
API_ENTREPRISE_TOKEN = ''  # ask SAR the token
API_ENTREPRISE_CONTEXT = 'Demande d\'embauche d\'un salarié étranger'
API_ENTREPRISE_OBJECT = 'Gestion Automatisée de l\'immigration professionnelle'
SIREN_DGEF = '130017593'


def request_wrapper(siret):
    url = 'https://entreprise.api.gouv.fr/v2/etablissements/{siret}/'.format(siret=siret)
    params = {
        'context': API_ENTREPRISE_CONTEXT,
        'recipient': SIREN_DGEF,
        'object': API_ENTREPRISE_OBJECT,
        'token': API_ENTREPRISE_TOKEN
    }
    return requests.get(url, params=params)
