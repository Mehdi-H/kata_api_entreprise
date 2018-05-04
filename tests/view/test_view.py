import json
from unittest.mock import patch

from pytest import fixture

from kata_api_entreprise.app import create_app


class TestEntrepriseApi:
    def setup_method(self, method):
        self.app = create_app(config='test')
        self.client = self.app.test_client()

    @fixture
    def setup_octo_data(self):
        octo_data = {"etablissement": {"siege_social": True, "siret": "41816609600069", "naf": "6202A",
                                       "libelle_naf": "Conseil en systèmes et logiciels informatiques",
                                       "date_mise_a_jour": 1505772000,
                                       "tranche_effectif_salarie_etablissement": {"de": 250, "a": 499,
                                                                                  "code": "32",
                                                                                  "date_reference": "2016",
                                                                                  "intitule": "250 à 499 salariés"},
                                       "date_creation_etablissement": 1480287600,
                                       "region_implantation": {"code": "11", "value": "Île-de-France"},
                                       "commune_implantation": {"code": "75102", "value": "PARIS 2"},
                                       "pays_implantation": {"code": None, "value": None},
                                       "diffusable_commercialement": True, "enseigne": None,
                                       "adresse": {"l1": "OCTO TECHNOLOGY", "l2": None, "l3": None,
                                                   "l4": "34 AVENUE DE L OPERA", "l5": None,
                                                   "l6": "75002 PARIS", "l7": "FRANCE", "numero_voie": "34",
                                                   "type_voie": "AV", "nom_voie": "DE L OPERA",
                                                   "complement_adresse": None, "code_postal": "75002",
                                                   "localite": "PARIS 2", "code_insee_localite": "75102",
                                                   "cedex": None}}, "gateway_error": False}
        return octo_data

    @fixture
    def setup_accenture_data(self):
        accenture_data = {"etablissement": {"siege_social": True, "siret": "73207531200122", "naf": "6202A",
                                            "libelle_naf": "Conseil en systèmes et logiciels informatiques",
                                            "date_mise_a_jour": 1501970400,
                                            "tranche_effectif_salarie_etablissement": {"de": 2000, "a": 4999,
                                                                                       "code": "51",
                                                                                       "date_reference": "2016",
                                                                                       "intitule": "2 000 à 4 999 salariés"},
                                            "date_creation_etablissement": 1044486000,
                                            "region_implantation": {"code": "11", "value": "Île-de-France"},
                                            "commune_implantation": {"code": "75113", "value": "PARIS 13"},
                                            "pays_implantation": {"code": None, "value": None},
                                            "diffusable_commercialement": True, "enseigne": None,
                                            "adresse": {"l1": "ACCENTURE", "l2": "118 122", "l3": None,
                                                        "l4": "118 AVENUE DE FRANCE", "l5": None,
                                                        "l6": "75636 PARIS CEDEX 13", "l7": "FRANCE",
                                                        "numero_voie": "118", "type_voie": "AV",
                                                        "nom_voie": "DE FRANCE", "complement_adresse": None,
                                                        "code_postal": "75013", "localite": "PARIS 13",
                                                        "code_insee_localite": "75113", "cedex": None}},
                          "gateway_error": False}
        return accenture_data

    def test_get_api_entreprise_returns_informations(self):
        # When
        response = self.client.get('/entreprise')

        # Then
        assert response.status_code == 404

    def test_404(self):
        # When
        response = self.client.get('/entreprise404')

        # Then
        assert response.status_code == 404

    def test_get_api_entreprise_octo_returns_200(self):
        # Given
        siret = 41816609600069

        # When
        response = self.client.get(f'/entreprise/{siret}')

        # Then
        assert response.status_code == 200

    def test_get_api_entreprise_octo_returns_type_json(self):
        # Given
        siret = 41816609600069

        # When
        response = self.client.get(f'/entreprise/{siret}')

        # Then
        assert response.mimetype == 'application/json'

    def test_get_api_entreprise_octo_returns_data_not_empty(self):
        # Given
        siret = 41816609600069

        # When
        response = self.client.get(f'/entreprise/{siret}')

        # Then
        assert len(response.data) != 0

    def test_get_api_entreprise_octo_siret_returns_good_data(self, setup_octo_data):
        # Given
        siret = 41816609600069

        # When
        response = self.client.get(f'/entreprise/{siret}')

        # Then
        assert setup_octo_data == json.loads(response.data)

    @patch("kata_api_entreprise.service.api_entreprise_service.request_wrapper")
    def test_get_api_entreprise_octo_siret_returns_good_stubed_data(self, request_wrapper, setup_octo_data):
        class MyToto:
            text = json.dumps(setup_octo_data)
            headers = {"Content-Type": "application/json"}

        # Given
        siret = 41816609600069
        request_wrapper.return_value = MyToto

        # When
        response = self.client.get(f'/entreprise/{siret}')

        # Then
        assert setup_octo_data == json.loads(response.data)

    def test_get_api_entreprise_with_bad_siret(self):
        # Given
        siret = 123

        # When
        response = self.client.get(f'/entreprise/{siret}')

        # Then
        print("response: " + str(response.data))
        assert 404 == response.status_code

    @patch("kata_api_entreprise.service.api_entreprise_service.request_wrapper")
    def test_request_wrapper_is_called_with_a_siret(self, request_wrapper, setup_accenture_data):
        class MyToto:
            text = json.dumps(setup_accenture_data)
            headers = {"Content-Type": "application/json"}

        # Given
        siret = '73207531200122'

        def side_effect(arg):
            assert arg == siret
            return MyToto

        request_wrapper.side_effect = side_effect

        # When
        self.client.get(f'/entreprise/{siret}')
