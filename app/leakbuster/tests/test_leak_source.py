from . import *
import json


class LeakSourceResourceTestWithAdminUser(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_new_leak(self):
        with app.test_client() as client:
            payload = {
                "author": "test",
                "date": "test",
                "description": "test",
                "url": "https://test.com"
            }
            response = client.post('/api/v2/leak/source/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_get_all(self):
        with app.test_client() as client:
            response = client.get('/api/v2/leak/source/', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(isinstance(response.json['data'], list))

    def test_get_leak_source(self):
        leak_id = add_testing_update_leak_source()

        with app.test_client() as client:
            response = client.get(f'/api/v2/leak/source/{leak_id}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_update_leak_source(self):
        leak_id = add_testing_update_leak_source()
        payload = {
                "author": "test",
                "date": "test",
                "description": "string",
                "url": "https://test.com"
            }
        with app.test_client() as client:
            response = client.put(f'/api/v2/leak/source/{leak_id}', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_del_leak_source(self):
        leak_id = add_testing_update_leak_source()
        with app.test_client() as client:
            response = client.delete(f'/api/v2/leak/source/{leak_id}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")


class LeakSourceResourceTestWithScriptUser(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_new_leak(self):
        with app.test_client() as client:
            payload = {
                "author": "test",
                "date": "test",
                "description": "test",
                "url": "https://test.com"
            }
            response = client.post('/api/v2/leak/source/', data=json.dumps(payload), headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

    def test_get_all(self):
        with app.test_client() as client:
            response = client.get('/api/v2/leak/source/', headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(isinstance(response.json['data'], list))

    def test_get_leak_source(self):
        leak_id = add_testing_update_leak_source()

        with app.test_client() as client:
            response = client.get(f'/api/v2/leak/source/{leak_id}', headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))


class LeakSourceErrorsTest(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_Unauthorized_Access(self):
        add_testing_update_user()
        endpoint_with_id = '/api/v2/leak/source/123456'
        endpoint = '/api/v2/leak/source/'

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

        leak_id = add_testing_update_leak_source()

        with app.test_client() as client:
            payload = {
                "date": "test",
                "url": "https://test.com"
            }
            response = client.post('/api/v2/leak/source/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.json['Message'])

            response = client.put(f'/api/v2/leak/source/{leak_id}', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.json['Message'])


    def test_error_404_wrong_leak_source_id(self):
        payload = {
            "author": "test",
            "date": "test",
            "description": "test",
            "url": "https://test.com"
        }
        with app.test_client() as client:
            response = client.put('/api/v2/leak/source/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Leak Source ID not found")

            response = client.get('/api/v2/leak/source/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Leak Source ID not found")

            response = client.delete('/api/v2/leak/source/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Leak Source ID not found")
