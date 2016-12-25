from rest_framework.test import APITestCase


# Create your tests here.
class VisitorAPITests(APITestCase):
    def test_visitor_get_api(self):
        response = self.client.get('/api/peopleinfo/')
        self.assertEqual(response.status_code, 200)

    def test_visitor_post_api(self):
        local_file_absolute_url = '/home/sud/Pictures/blur.png'
        image_file = open(local_file_absolute_url, 'rb')
        data = {
            "name": "sudhanshu",
            "email": "mailbox.sud@gmail.com",
            "phone": "9930289385",
            "whom_to_meet": "aniket",
            "company_name": "corseco",
            "photo": image_file
        }
        response = self.client.post('/api/peopleinfo/',
                                    data,
                                    format='multipart')
        self.assertEqual(response.status_code, 201)
