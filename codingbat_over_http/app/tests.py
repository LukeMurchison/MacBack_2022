from django.test import SimpleTestCase

# Create your tests here.

class TestHelloView(SimpleTestCase):
    def test_near_hundred_90(self):
        response = self.client.get("/near_hundred/90/")
        self.assertContains(response, "True")
    def test_near_hundred_210(self):
        response = self.client.get("/near_hundred/210/")
        self.assertContains(response, "True")
    def test_near_hundred_30(self):
        response = self.client.get("/near_hundred/30/")
        self.assertContains(response, "False")

    def test_string_splosion_ab(self):
        response = self.client.get("/string_splosion/ab/")
        self.assertContains(response, "aab")
    def test_string_splosion_code(self):
        response = self.client.get("/string_splosion/code/")
        self.assertContains(response, "ccocodcode")
    def test_string_splosion_x(self):
        response = self.client.get("/string_splosion/x/")
        self.assertContains(response, "x")

    def test_cat_dog_catdog(self):
        response = self.client.get("/cat_dog/catdog/")
        self.assertContains(response, "True")
    def test_cat_dog_catcat(self):
        response = self.client.get("/cat_dog/catcat/")
        self.assertContains(response, "False")
    def test_cat_dog_catxdogxdogxcat(self):
        response = self.client.get("/cat_dog/catxdogxdogxcat/")
        self.assertContains(response, "True")

    def test_lone_sum_1_2_3(self):
        response = self.client.get("/lone_sum/1/2/3/")
        self.assertContains(response, "6")
    def test_lone_sum_3_3_3(self):
        response = self.client.get("/lone_sum/3/3/3/")
        self.assertContains(response, "0")
    def test_lone_sum_2_2_9(self):
        response = self.client.get("/lone_sum/2/2/9/")
        self.assertContains(response, "9")

    
