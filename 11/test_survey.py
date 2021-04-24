
import unittest
from survey import AnonymousSurvey

class TestAnonimousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_servey = AnonymousSurvey(question)
        my_servey.store_response('English')
        self.assertIn('English', my_servey.responses)

    def test_store_three_response(self):
        question = "What language did you first learn to speak?"
        my_servey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_servey.store_response(response)

        for response in responses:
            self.assertIn(response, my_servey.responses)

if __name__ in '__main__':
    unittest.main()




