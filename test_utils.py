import unittest

from utils import slugify, truncate


class SlugifyTests(unittest.TestCase):
    def test_example_phrase(self):
        self.assertEqual(slugify("Hello, Relay World!"), "hello-relay-world")

    def test_empty_input(self):
        self.assertEqual(slugify(""), "")

    def test_repeated_separators(self):
        self.assertEqual(slugify("foo---bar"), "foo-bar")
        self.assertEqual(slugify("a   b"), "a-b")


class TruncateTests(unittest.TestCase):
    def test_example_phrase(self):
        self.assertEqual(truncate("Hello Relay World", 12), "Hello Relay…")

    def test_fits_unchanged(self):
        self.assertEqual(truncate("short", 10), "short")

    def test_empty_input(self):
        self.assertEqual(truncate("", 5), "")

    def test_single_word_longer_than_max_len(self):
        self.assertEqual(truncate("superlongword", 5), "supe…")

    def test_custom_suffix(self):
        self.assertEqual(truncate("Hello Relay World", 14, "..."), "Hello Relay...")


if __name__ == "__main__":
    unittest.main()
