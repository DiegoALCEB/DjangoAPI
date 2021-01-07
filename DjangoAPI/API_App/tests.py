from django.test import TestCase, Client

# Create your tests here.

class APITestCase(TestCase):
    #GET ALL ARTICLES
    def test_api_get(self):
        client = Client()
        response = client.get("/api/articles")
        self.assertEqual(response.status_code, 200)

    #PUT A ARTICLE
    def test_api_post(self):
        client = Client()
        response = client.post("/api/articles")
        self.assertEqual(response.status_code, 200)

    #GET AN ARTICLE BY ID
    def test_api_get_by_id(self):
        client = Client()
        response = client.get("/api/articles/1")
        self.assertEqual(response.status_code, 200)

    #UPDATE AN ARTICLE BY ID
    def test_api_update_by_id(self):
        client = Client()
        response = client.put("/api/articles/1")
        self.assertEqual(response.status_code, 200)

    #DELETE AN ARTICLE BY ID
    def test_api_delete_by_id(self):
        client = Client()
        response = client.delete("/api/articles/1")
        self.assertEqual(response.status_code, 200)