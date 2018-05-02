from unittest import TestCase

from kata_api_entreprise.view import create_app


class TestEntrepriseApi(TestCase):
    def setup_method(self, method):
        self.app = create_app(config='test')
        self.client = self.app.test_client()

    def test_get_api_entreprise_returns_informations(self):
        rv = self.client.get('/')
        self.assertEqual(rv.data, b'Hello, World!')
        self.assertEqual(rv.status_code, 200)
