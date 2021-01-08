from django.test import TestCase, Client
from .models import Article
import json

# Create your tests here.

class APITestCase(TestCase):

    ###### Server side test
    
    def setUp(self):
        #Create some articles
        Article.objects.create(name = "ART1", description = "DESC1")
        Article.objects.create(name = "ART2", description = "DESC2")
    
    def test_get_all_articles(self):
        self.assertEqual(Article.objects.all().count(), 2)
    
    ###### Client side test

    #GET ALL ARTICLES
    def test_api_get(self):
        client = Client()
        response = client.get("/api/articles")
        self.assertEqual(response.status_code, 200)
        responsejson = json.loads(response.json()['articles'])
        self.assertEqual(len(responsejson), 2)
        self.assertEqual(responsejson[0]['fields']['name'], "ART1")
        self.assertEqual(responsejson[0]['fields']['description'], "DESC1")
        self.assertEqual(responsejson[1]['fields']['name'], "ART2")
        self.assertEqual(responsejson[1]['fields']['description'], "DESC2")

    #PUT A ARTICLE
    def test_api_post(self):
        client = Client()
        response = client.post("/api/articles", {'name': 'ART3', 'description': 'DESC3'}, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    #GET AN ARTICLE BY ID
    def test_api_get_by_id(self):
        client = Client()
        response = client.get("/api/articles/1")
        self.assertEqual(response.status_code, 200)
        responsejson = json.loads(response.json()['article'])
        self.assertEqual(len(responsejson), 1)
        self.assertEqual(responsejson[0]['fields']['name'], "ART1")
        self.assertEqual(responsejson[0]['fields']['description'], "DESC1")
