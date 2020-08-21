import unittest
import reverse_one_line_nested_dictionary as reverse

class ReverseTestCase(unittest.TestCase):
    def setUp(self):
        self.input_value = {
          'hired': {
            'be': {
              'to': {
                'deserve': 'I'
              }
            }
          }
        }

        self.output_value = {
          'I': {
            'deserve': {
              'to': {
                 'be': 'hired'
              }
            }
          }
        }
    
    def tearDown(self):
        pass

    def test_reverse(self):
        result = reverse.answer(self.input_value)
        self.assertEqual(self.output_value, result)

if __name__ == "__main__":
    unittest.main()

