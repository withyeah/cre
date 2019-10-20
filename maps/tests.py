from rest_framework.test import APITestCase

# Create your tests here.

class RegionTests(APITestCase):

    def setUp(self):
        self.region_name = '강남구/'
        self.region_code = '8211170101'

    def test_region_detail(self):
        url = f'https://cre-region.herokuapp.com/region/{self.region_name}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_father(self):
        url = f'https://cre-region.herokuapp.com/region/{self.region_code}/father/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class DocsTests(APITestCase):

    def test_redoc(self):
        url = 'https://cre-region.herokuapp.com/region/redoc/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_swagger(self):
        url = 'https://cre-region.herokuapp.com/region/swagger/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
