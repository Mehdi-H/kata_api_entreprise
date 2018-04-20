from unittest import TestCase
from kata_api_entreprise import app


class TestHello(TestCase):
    def test_hello(self):
        # Given
        app.testing = True
        self.app = app.test_client()

        # When
        response = self.app.get('/entreprise')

        # Then
        assert response.status_code == 404
