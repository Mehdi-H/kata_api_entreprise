import json
from unittest import TestCase

from kata_api_entreprise.view import create_app


# http://anef.scille.eu/gaip-1-employeur/#/
class TestEntrepriseApi(TestCase):
    def setup_method(self, method):
        self.app = create_app(config='test')
        self.client = self.app.test_client()

    def test_get_api_entreprise_returns_informations(self):
        response = self.client.get('/entreprise/41816609600069')
        assert response.status_code == 200
        assert json.loads(response.data) == {
            'etablissement': {'adresse': {'cedex': None,
                                          'code_insee_localite': '75102',
                                          'code_postal': '75002',
                                          'complement_adresse': None,
                                          'l1': 'OCTO TECHNOLOGY',
                                          'l2': None,
                                          'l3': None,
                                          'l4': '34 AVENUE DE L OPERA',
                                          'l5': None,
                                          'l6': '75002 PARIS',
                                          'l7': 'FRANCE',
                                          'localite': 'PARIS 2',
                                          'nom_voie': 'DE L OPERA',
                                          'numero_voie': '34',
                                          'type_voie': 'AV'},
                              'commune_implantation': {'code': '75102',
                                                       'value': 'PARIS 2'},
                              'date_creation_etablissement': 1480287600,
                              'date_mise_a_jour': 1505772000,
                              'diffusable_commercialement': True,
                              'enseigne': None,
                              'libelle_naf': 'Conseil en systèmes et logiciels '
                                             'informatiques',
                              'naf': '6202A',
                              'pays_implantation': {'code': None, 'value': None},
                              'region_implantation': {'code': '11',
                                                      'value': 'Île-de-France'},
                              'siege_social': True,
                              'siret': '41816609600069',
                              'tranche_effectif_salarie_etablissement': {'a': 499,
                                                                         'code': '32',
                                                                         'date_reference': '2016',
                                                                         'de': 250,
                                                                         'intitule': '250 '
                                                                                     'à '
                                                                                     '499 '
                                                                                     'salariés'}},
            'gateway_error': False
        }
