import unittest
from unittest.mock import patch, mock_open
from main import validate_domain, process_domains_from_file, fetch_domains_from_url


class TestDomainValidation(unittest.TestCase):
    def test_validate_domain(self):
        self.assertTrue(validate_domain("example.com"))
        self.assertTrue(validate_domain("sub-domain.org"))
        self.assertFalse(validate_domain("invalid_domain"))
        self.assertFalse(validate_domain("-invalid.com"))
        self.assertFalse(validate_domain("invalid-.com"))

    def test_process_domains_from_file(self):
        mock_file_content = "example.com\ninvalid_domain\nvalid-site.net\n"
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            valid_domains = process_domains_from_file("mock_file.txt")
        self.assertEqual(valid_domains, ["example.com", "valid-site.net"])


if __name__ == "__main__":
    unittest.main()
