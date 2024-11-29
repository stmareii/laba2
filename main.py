import re

# Регулярное выражение для доменных имен
DOMAIN_REGEX = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$'

def validate_domain(domain):
    #Проверка доменного имени.
    return re.match(DOMAIN_REGEX, domain) is not None

def read_domains_from_file(file_path):
    #Чтение доменных имен из файла.
    with open(file_path, 'r', encoding='utf-8') as file:
        domains = file.readlines()
    # Убираем лишние пробелы и символы новой строки
    return [domain.strip() for domain in domains]


def process_domains_from_file(input_file):
    #Чтение доменов из файла, проверка и запись корректных доменов.
    domains = read_domains_from_file(input_file)
    valid_domains = [domain for domain in domains if validate_domain(domain)]
    return valid_domains

if __name__ == "__main__":
    input_file = "domains.txt"  # Входной файл с доменами
    print(f"Чтение доменных имен из файла: {input_file}")
    valid_domains = process_domains_from_file(input_file)
    print("Список корректных доменов:")
    for domain in valid_domains:
        print(domain)
