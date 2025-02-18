import unittest
import json
import os
from docx import Document
from app import fill_template

class FillTemplateTestCase(unittest.TestCase):
    def setUp(self):
        # Adjust the path to the test.json file
        app_dir = os.path.dirname(os.path.abspath(__file__))
        test_json_path = os.path.join(app_dir, '..', 'test.json')

        with open(test_json_path) as f:
            self.data = json.load(f)
        self.template_path = os.path.join(app_dir, '..', 'obrazac.docx')
        self.output_path = os.path.join(app_dir, 'filled_obrazac_test.docx')

    def test_fill_template(self):
        fill_template(self.data, self.template_path, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

if __name__ == '__main__':
    unittest.main()
