from django.test import TestCase, Client

#
# print(response)
class Phase1(TestCase):
    def setUp(self):
        self.twiml_enter_a_number = "<?xml version=\"1.0\" encoding=\"UTF-8\"?> \
                                    <Response> \
                                        <Gather input=\"speech dtmf\" timeout=\"3\" numDigits=\"1\">\
                                            <Say>Please press 1 or say sales for sales.</Say>\
                                        </Gather>\
                                    </Response>"

        self.twiml_fizzbuzz_up_to_10 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?> \
                                        <Response> \
                                            <Say voice=\"woman\" language=\"en\">1</Say> \
                                            <Say voice=\"woman\" language=\"en\">2</Say> \
                                            <Say voice=\"woman\" language=\"en\">3</Say> \
                                            <Say voice=\"woman\" language=\"en\">4</Say> \
                                            <Say voice=\"woman\" language=\"en\">5</Say> \
                                            <Say voice=\"woman\" language=\"en\">6</Say> \
                                            <Say voice=\"woman\" language=\"en\">7</Say> \
                                            <Say voice=\"woman\" language=\"en\">8</Say> \
                                            <Say voice=\"woman\" language=\"en\">9</Say> \
                                            <Say voice=\"woman\" language=\"en\">10</Say> \
                                        </Response>"

    def test_enter_a_number(self):
        client = Client()

        response = client.get("twimlgen:enter_number")
        print response.body

        self.assertEqual(response.body, self.twiml_enter_a_number)

