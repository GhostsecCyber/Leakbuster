from . import *
import json
import responses


class LeakGeneralResourceTestWithAdminUser(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    @responses.activate
    def test_new_leak_general(self):
        self.leakSourceID = add_testing_update_leak_source()
        responses.add(responses.GET, 'http://test.com', status=200, body="test")
        with app.test_client() as client:
            payload = {
                "url": "http://test.com",
                "leak_id": self.leakSourceID
            }
            response = client.post('/api/v2/leak/general/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))
            os.remove(decrypt(f"{response.json['data']['leaks']}"))

    def test_get_all(self):
        general_id = add_testing_general_leak()
        with app.test_client() as client:
            response = client.get('/api/v2/leak/general/', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(isinstance(response.json['data'], list))

        LeakGeneralMD.query.get_or_404(general_id).delete()

    def test_get_leak_general(self):
        general_id = add_testing_general_leak()
        with app.test_client() as client:
            response = client.get(f'/api/v2/leak/general/{general_id}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))

        LeakGeneralMD.query.get_or_404(general_id).delete()

    def test_del_leak_general(self):
        general_id = add_testing_general_leak()
        with app.test_client() as client:
            response = client.delete(f'/api/v2/leak/general/{general_id}', headers=default_header())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json['Status'], "Success")


class LeakGeneralResourceTestWithScriptUser(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    @responses.activate
    def test_new_leak_general(self):
        self.leakSourceID = add_testing_update_leak_source()
        responses.add(responses.GET, 'http://test.com', status=200)
        with app.test_client() as client:
            payload = {
                "url": "http://test.com",
                "leak_id": self.leakSourceID
            }
            response = client.post('/api/v2/leak/general/', data=json.dumps(payload), headers=script_user_header())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['Status'], "Success")
            self.assertTrue(isinstance(response.json['data'], dict))
            os.remove(decrypt(f"{response.json['data']['leaks']}"))


class LeakGeneralErrorsTest(ProjectTest):
    def setUp(self):
        super().setUp()
        add_testing_user()

    def test_Unauthorized_Access(self):
        add_testing_update_user()
        endpoint_with_id = '/api/v2/leak/general/123456'
        endpoint = '/api/v2/leak/general/'

        response = []

        with app.test_client() as client:
            response.append(client.get(endpoint, headers=wrong_header()))
            response.append(client.post(endpoint, headers=wrong_header()))

            response.append(client.get(endpoint_with_id, headers=wrong_header()))
            response.append(client.delete(endpoint_with_id, headers=wrong_header()))

            response.append(client.get(endpoint, headers=default_user_header()))
            response.append(client.post(endpoint, headers=default_user_header()))

            response.append(client.get(endpoint_with_id, headers=default_user_header()))
            response.append(client.delete(endpoint_with_id, headers=default_user_header()))

            response.append(client.delete(endpoint_with_id, headers=script_user_header()))
            response.append(client.get(endpoint, headers=script_user_header()))
            response.append(client.get(endpoint_with_id, headers=script_user_header()))

            for resp in response:
                self.assertEqual(resp.status_code, 401)


    def test_error_400_missing_parameters(self):

        general_id = add_testing_general_leak()

        with app.test_client() as client:
            payload = {
                "url": "https://test.com"
            }
            response = client.post('/api/v2/leak/general/', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(response.json['Message'])

        LeakGeneralMD.query.get_or_404(general_id).delete()

    def test_error_404_wrong_leak_general_id(self):

        payload = {
            "url": "http://test.com",
            "leak_id": "123456"
        }
        with app.test_client() as client:

            response = client.get('/api/v2/leak/general/50', data=json.dumps(payload), headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Leak Content ID not found")

            response = client.delete('/api/v2/leak/general/50', headers=default_header())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(response.json['Message'], "Leak Content ID not found")
