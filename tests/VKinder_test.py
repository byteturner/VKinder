import unittest
from unittest.mock import Mock, patch

import app.custom_functions


class TestVKinder(unittest.TestCase):

    def test_init_user(self):
        data = {'sex': 2, 'bdate': '15.9.1993',
                'city': {'id': 53, 'title': 'Жуковский'},
                'country': {'id': 1, 'title': 'Россия'}}
        with patch('app.custom_functions.get_user_info', return_value=data):
            with patch('app.custom_functions.get_token', return_value='11111111'):
                with patch('app.custom_functions.make_request') as r_mock:
                    m_mock = Mock()
                    m_mock.json.return_value = {'response': [{'id': '2222222'}]}
                    r_mock.return_value = m_mock
                    user1 = app.custom_functions.User('anonym')
                    self.assertEqual(user1.user_sex, data['sex'])

    def test_get_photos(self):
        request_data = {'count': 53}
        with patch('app.custom_functions.make_request') as r_mock:
            m_mock = Mock()
            m_mock.json.return_value = {'response': request_data}
            r_mock.return_value = m_mock
            result = app.custom_functions.get_photos('token', 'id')
            self.assertEqual(request_data['count'], result['response']['count'])


if __name__ == '__main__':
    unittest.main()
