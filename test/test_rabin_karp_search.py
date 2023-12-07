import unittest

from app.src.rabin_karp_search import rabinKarpSearch


class TestRabinKarpSearch(unittest.TestCase):

    def test_search(self):
        haystack = "adcasdabcasabc"
        needle = "abc"
        prime_number = 101

        result = rabinKarpSearch(needle, haystack, prime_number)
        self.assertEqual(result, [6, 11])