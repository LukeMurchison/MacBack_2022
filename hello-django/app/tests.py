from django.test import SimpleTestCase

# Create your tests here.

class TestHelloView(SimpleTestCase):
    def test_hello_nate(self):
        response = self.client.get("/hello/")
        self.assertContains(response, "Hello World!")
