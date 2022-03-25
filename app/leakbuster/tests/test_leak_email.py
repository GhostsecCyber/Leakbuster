from . import *
import json


class LeakEmailResourceTestWithAdminUser(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_new_email_leak(self):
        self.leakSourceID = add_testing_update_leak_source()
        with app.test_client() as client:
            payload = {
                "email": "unit_test@test.com.br",
                "leak_id": self.leakSourceID,
                "leak_password": "test"
            }
            response = client.post('/api/v2/leak/email/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_get_all(self):
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()
        with app.test_client() as client:
            response = client.get('/api/v2/leak/email/', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(isinstance(response.json['data'], list))

    def test_get_email_leak(self):
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()
        with app.test_client() as client:
            response = client.get(f'/api/v2/leak/email/{self.leakEmailID}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_update_email_leak(self):
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()
        payload = {
                "email": "unit_test_updated@test.com.br",
                "leak_id": self.leakSourceID,
                "leak_password": "test"
            }
        with app.test_client() as client:
            response = client.put(f'/api/v2/leak/email/{self.leakEmailID}', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_del_email_leak(self):
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()
        with app.test_client() as client:
            response = client.delete(f'/api/v2/leak/email/{self.leakEmailID}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")


class LeakEmailResourceTestWithScriptUser(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_new_email_leak(self):
        self.leakSourceID = add_testing_update_leak_source()
        with app.test_client() as client:
            payload = {
                "email": "unit_test@test.com.br",
                "leak_id": self.leakSourceID,
                "leak_password": "test"
            }
            response = client.post('/api/v2/leak/email/', data=json.dumps(payload), headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_get_all(self):
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()
        with app.test_client() as client:
            response = client.get('/api/v2/leak/email/', headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(isinstance(response.json['data'], list))

    def test_get_email_leak(self):
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()
        with app.test_client() as client:
            response = client.get(f'/api/v2/leak/email/{self.leakEmailID}', headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))


class LeakEmailErrorsTest(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()
        self.leakEmailID, self.leakSourceID = add_testing_update_leak_email()

    def test_Unauthorized_Access(self):
        add_testing_update_user()
        endpoint_with_id = '/api/v2/leak/email/123456'
        endpoint = '/api/v2/leak/email/'

        response = []

        with app.test_client() as client:
            response.append(client.get(endpoint, headers=wrong_header()))
            response.append(client.post(endpoint, headers=wrong_header()))

            response.append(client.get(endpoint_with_id, headers=wrong_header()))
            response.append(client.put(endpoint_with_id, headers=wrong_header()))
            response.append(client.delete(endpoint_with_id, headers=wrong_header()))

            response.append(client.get(endpoint, headers=default_user_header()))
            response.append(client.post(endpoint, headers=default_user_header()))

            response.append(client.get(endpoint_with_id, headers=default_user_header()))
            response.append(client.put(endpoint_with_id, headers=default_user_header()))
            response.append(client.delete(endpoint_with_id, headers=default_user_header()))

            response.append(client.put(endpoint_with_id, headers=script_user_header()))
            response.append(client.delete(endpoint_with_id, headers=script_user_header()))

            for resp in response:
                self.assertEqual(resp.status_code, 401)

    def test_error_400_missing_parameters(self):

        with app.test_client() as client:
            payload = {
                "email": "unit_test@test.com.br",
                "leak_password": "test"
            }
            response = client.post('/api/v2/leak/email/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.json['Message'])

            response = client.put(f'/api/v2/leak/email/{self.leakEmailID}', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.json['Message'])

    def test_error_404_wrong_leak_source_id(self):
        payload = {
            "email": "unit_test@test.com.br",
            "leak_id": self.leakSourceID,
            "leak_password": "test"
        }
        with app.test_client() as client:
            response = client.put('/api/v2/leak/email/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Mail ID not found")

            response = client.get('/api/v2/leak/email/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Mail ID not found")

            response = client.delete('/api/v2/leak/email/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Mail ID not found")
