import unittest

from flaskapp import app
from redis import Redis

class CounterTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    def tearDown(self):
        pass

    # actual tests
    def test_welcome_page(self):
        """ test that assesses my index '/' route works """
        reponse = self.app.get('/')
        #http status code == 200
        self.assertEqual(reponse.status_code, 200)

    def test_redis_connection(self):
        redis = Redis(host='redis-server', db=0)
        self.app.get('/visit')
        self.assertEqual(int(redis.get("coutner")), 1)

if __name__ == "__main__":
    unittest.main()

