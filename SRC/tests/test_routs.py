import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #

    # AN HTML PAGE IS RETURNED
    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #

    # JSON IS RETURNED
    def test_get_list_route(self):
        response = self.app.get('/get_list')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #

    # HTML IS RETURNED
    def test_clinic_get_route(self):
        response = self.app.get('/clinic')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #

    # THIS WAS WRITTEN WITH AI (IDK ABOUT STATUS CODES)
    def test_clinic_post_route(self):
        data = {
            'name': 'John Doe',
            'age': '30',
            'symptoms': 'cough, fever'
        }
        response = self.app.post('/clinic', data=data)
        self.assertEqual(response.status_code, 302)

    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #

    # HTML
    def test_hospital_get_route(self):
        response = self.app.get('/hospital')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #

    # STATUS CODE
    def test_hospital_post_route(self):
        data = {
            'record_id': '1',
            'result': 'positive',
            'prescription': 'antibiotics'
        }
        response = self.app.post('/hospital', data=data)
        self.assertEqual(response.status_code, 302)








if __name__ == '__main__':
    unittest.main()