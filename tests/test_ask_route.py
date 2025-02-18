import unittest
from app import app

class AskRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ask_route(self):
        payload = {
            "naziv_predmeta": "Mašinsko učenje",
            "studijski_program": "Podatkovne znanosti",
            "ects_bodovi": 6,
            "ciklus": 1,
            "godina_studija": 1,
            "kod_predmeta": "MZ101",
            "predavanja": 30,
            "vjezbe": 15,
            "seminari": 5,
            "praksa": 20,
            "vizija":  "Cilj predmeta je upoznavanje studenata s osnovnim konceptima mašinskog učenja.",
            "ishodi":  "Studenti će biti osposobljeni za samostalno korištenje algoritama mašinskog učenja."
        }

        response = self.app.post('/ask', json=payload)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
