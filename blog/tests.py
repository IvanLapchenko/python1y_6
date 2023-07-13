from unittest.mock import Mock
from django.test import TestCase
from django.contrib.messages import get_messages


class TestViews(TestCase):
    def setUp(self) -> None:
        self.url = 'http://localhost:8000'

    def test_render_main_page_with_category_id(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('main.html')

    def test_dont_create_question(self):
        question = {'text': 'test', 'title': 'test', 'category': 1}

        response = self.client.post('/create_question', data=question, user=1)
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(len(messages) > 0)

