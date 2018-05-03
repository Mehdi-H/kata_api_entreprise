from kata_api_entreprise.app import create_app


class TestEntrepriseApi:
    def setup_method(self, method):
        self.app = create_app(config='test')
        self.client = self.app.test_client()

    def test_get_api_entreprise_returns_informations(self):
        # Given

        # When
        response = self.client.get('/entreprise')

        # Then
        assert response.status_code == 200
        assert response.data == b'Hello World !'


# OCTO siret : 41816609600069
# URL apientreprise : https://entreprise.api.gouv.fr/v2/etablissements/41816609600069?token=p9A9funz6VJZGy1ZWI3d6aBIMJqIpcSB&context='Demande d\'embauche d\'un salarié étranger'&object='Gestion Automatisée de l\'immigration professionnelle'&recipient='130017593'