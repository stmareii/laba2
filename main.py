import re
import requests

# Регулярное выражение для проверки доменных имен
DOMAIN_REGEX = r"https?:\/\/[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})*|[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}"


def validate_domain(domain):
    # Проверка синтаксической корректности доменного имени.
    return re.match(DOMAIN_REGEX, domain) is not None


def read_domains_from_file(file_path):
    # Чтение доменных имен из файла.
    with open(file_path, "r", encoding="utf-8") as file:
        domains = file.readlines()
    return [domain.strip() for domain in domains]


def process_domains_from_file(input_file):
    # Проверка доменных имен из файла.
    domains = read_domains_from_file(input_file)
    return [domain for domain in domains if validate_domain(domain)]


def validate_domains_from_input():
    # Проверка доменных имен через пользовательский ввод.
    print(
        "Введите доменные имена (по одному на строке). Для завершения введите пустую строку."
    )
    user_domains = []
    while True:
        domain = input("Введите домен: ").strip()
        if not domain:
            break
        user_domains.append(domain)

    valid_domains = [domain for domain in user_domains if validate_domain(domain)]
    print("\nКорректные доменные имена:")
    for domain in valid_domains:
        print(domain)


if __name__ == "__main__":
    print("Выберите действие:")
    print("1. Проверить доменные имена из файла")
    print("2. Проверить доменные имена через ввод пользователя")
    choice = input("Введите номер действия: ").strip()

    if choice == "1":
        input_file = input("Введите название файла: ").strip()
        valid_domains = process_domains_from_file(input_file)
        print("\nКорректные доменные имена из файла:")
        for domain in valid_domains:
            print(domain)
    elif choice == "2":
        validate_domains_from_input()
    else:
        print("Некорректный выбор.")
