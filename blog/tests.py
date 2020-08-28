from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Post

class PostTest(TestCase):

    def test_home_status(self):
        self.helper_tests('home', 'home.html')
    
    
    def helper_tests(self, url_name, template_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

        
class TestModels(TestCase):

    def setUp(self):
        
        self.user = get_user_model().objects.create_user(
            username="test",
            email="test@email.com",
            password="testing123456"
        )
        
        self.post = Post(
            title="Cooking good food",
            author=self.user,
            body="Cooking is my favorite thing to do. Today, I am preparing a delicious home made something. I actually don't know how to cook anything!"
        )
        
        self.post.save()


    def test_post(self):
        
        detail = Post.objects.get(pk=1)

        self.assertEqual(detail, self.post)

    
