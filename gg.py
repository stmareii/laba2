import unittest
import os
from main import validate_domain, process_domains_from_file


class TestFileDomainProcessing(unittest.TestCase):
    def setUp(self):
        # Создание временного входного файла.
        self.input_file = "test_domains.txt"
        self.output_file = "test_valid_domains.txt"

    def test_process_domains_from_file(self):
        # Тестирование обработки доменов из файла.
        valid_domains = process_domains_from_file(self.input_file, self.output_file)
        self.assertEqual(valid_domains, ["example.com", "valid-domain.org"])

        # Проверяем, что выходной файл содержит только корректные домены
        with open(self.output_file, "r", encoding="utf-8") as file:
            output_content = file.read().strip().split("\n")
        self.assertEqual(output_content, ["example.com", "valid-domain.org"])


if __name__ == "__main__":
    unittest.main()
