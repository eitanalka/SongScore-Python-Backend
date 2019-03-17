import unittest
import sys
from app import create_app

class TestApp(unittest.TestCase):
  def setUp(self):
    self.app = create_app().test_client()

  def test_classify_lyrics_success(self):
    response = self.app.post('/classify-lyrics', json={
      'lyrics': 'that you only meant well'
    })
    status = response.status_code
    self.assertEqual(status, 200)
    json_data = response.get_json()
    self.assertEqual(json_data, {'artist': 'jason derulo', 'song': 'whatcha say'})

  def test_classify_lyrics_fail(self):
    response = self.app.post('/classify-lyrics', json={})
    status = response.status_code
    self.assertEqual(status, 400)
    data = str(response.get_data())
    self.assertIn('Must include lyrics field in body', data)

if __name__ == '__main__':
    unittest.main()
