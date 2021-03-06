from . import *
import json


class UserResourceTest(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_new_user(self):
        with app.test_client() as client:
            payload = {
                "cdomain": "@string.com",
                "company": "string",
                "email": "string@mail.com",
                "name": "string",
                "password": "string",
                "phone": "string",
                "roles": "user",
                "site": "http://string.com"
            }
            response = client.post('/api/v2/user/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_get_all(self):
        with app.test_client() as client:
            response = client.get('/api/v2/user/', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(isinstance(response.json['data'], list))

    def test_get_user(self):
        user_id = add_testing_update_user()

        with app.test_client() as client:
            response = client.get(f'/api/v2/user/{user_id}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_update_user(self):
        user_id = add_testing_update_user()
        payload = {
            "cdomain": "@string.com",
            "company": "string",
            "email": "string@mail.com",
            "name": "string",
            "password": "string",
            "phone": "string",
            "site": "http://string.com"
        }
        with app.test_client() as client:
            response = client.put(f'/api/v2/user/{user_id}', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_del_user(self):
        user_id = add_testing_update_user()
        with app.test_client() as client:
            response = client.delete(f'/api/v2/user/{user_id}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")


class UserErrorsTest(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_Unauthorized_Access(self):
        add_testing_update_user()
        response = []
        with app.test_client() as client:
            response.append(client.get('/api/v2/user/', headers=wrong_header()))
            response.append(client.get('/api/v2/user/123456', headers=default_user_header()))

            for resp in response:
                self.assertEqual(resp.status_code, 401)

    def test_error_400_missing_parameters(self):
        user_id = add_testing_update_user()
        response = []
        with app.test_client() as client:
            payload = {
                "name": "updated_user",
                "password": "password",
                "admin": True,
                "group": []
            }
            response.append(client.post('/api/v2/user/', headers=default_header()))
            response.append(client.put(f'/api/v2/user/{user_id}', headers=default_user_header()))

            for resp in response:
                self.assertEqual(resp.status_code, 400)

    def test_error_404_wrong_user_id(self):
        payload = {
            "cdomain": "@string.com",
            "company": "string",
            "email": "string@mail.com",
            "name": "string",
            "password": "string",
            "phone": "string",
            "site": "http://string.com"
        }
        response = []
        with app.test_client() as client:
            response.append(client.put('/api/v2/user/50', data=json.dumps(payload), headers=default_header()))

            response.append(client.delete('/api/v2/user/50', headers=default_header()))

            for resp in response:
                self.assertEqual(resp.status_code, 404)
                self.assertTrue(resp.json['Message'], "User ID not found")
