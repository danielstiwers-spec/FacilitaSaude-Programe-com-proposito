from django.test import TestCase


class HomeAndLoginViewsTests(TestCase):
    def test_home_page_is_available(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_is_available(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form_can_create_a_user(self):
        response = self.client.post('/cadastro/', {
            'cpf': '12345678900',
            'rg': '1234567',
            'email': 'teste@example.com',
            'senha': 'senha123',
        })
        self.assertEqual(response.status_code, 302)
