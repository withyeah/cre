# Backend Project_Alex

> 20191020
>
> Deployed on Heroku : https://cre-region.herokuapp.com/
>
> code on GitHub : https://github.com/withyeah/cre



## Endpoints

1. `GET /region/<region_name>` :

   > example)
   >
   > /region/seoul
   >
   > ![image](https://user-images.githubusercontent.com/45819975/67157554-87ae3480-f368-11e9-9f6f-0e88a01d93be.png)

2. `GET /region/<region_code>/father/` :

   > example)
   >
   > /region/8211170101/father/
   >
   > ![image](https://user-images.githubusercontent.com/45819975/67157576-df4ca000-f368-11e9-8698-93525c2727f7.png)

   

## API Docs

1. `GET /region/redoc/` : redoc

2. `GET /region/swagger/` : swagger

   ![image](https://user-images.githubusercontent.com/45819975/67157509-3140f600-f368-11e9-973f-5e1e6e39ca91.png)



## Unit Tests

```shell
$ pytest
```

```python
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
```

