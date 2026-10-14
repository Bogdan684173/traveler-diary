
# diary.py — Щоденник мандрівника

diary = [
    {
        "day": 1,
        "text": "Прибув до містечка Вербівка, зупинився на заїжджому дворі."
    },
    {
        "day": 2,
        "text": "Знайшов стару карту в руїнах на околиці міста."
    },
]

def entries_with_word(diary, word):
    """Знаходить записи, які містять задане слово."""
    found_entries = []

    for entry in diary:
        if word.lower() in entry["text"].lower():
            found_entries.append(entry)

    return found_entries

    
def print_diary(diary):
    """Виводить усі записи щоденника."""
    print("\n=== Щоденник мандрівника ===")

    for entry in diary:
        print(f"День {entry['day']}: {entry['text']}")


def add_entry(diary):
    """Додає новий запис до щоденника."""
    print("\n=== Новий запис ===")

    text = input("Опиши свою пригоду: ").strip()

    if text == "":
        print("Помилка: запис не може бути порожнім.")
        return

    new_entry = {
        "day": len(diary) + 1,
        "text": text
    }

    diary.append(new_entry)

    print("Новий запис успішно додано!")


def entries_with_word(diary, word):
    """Знаходить записи, які містять задане слово."""
    found_entries = []

    for entry in diary:
        if word.lower() in entry["text"].lower():
            found_entries.append(entry)

    return found_entries


def search_entries(diary):
    """Шукає записи за словом."""
    word = input("Введи слово для пошуку: ").strip()

    if word == "":
        print("Введи слово для пошуку.")
        return

    results = entries_with_word(diary, word)

    if len(results) == 0:
        print("Записів із таким словом не знайдено.")
    else:
        print("\n=== Результати пошуку ===")

        for entry in results:
            print(f"День {entry['day']}: {entry['text']}")


def main():
    """Головне меню програми."""
    while True:
        print("\n=== Щоденник мандрівника ===")
        print("1. Переглянути записи")
        print("2. Додати запис")
        print("3. Знайти запис за словом")
        print("4. Вийти")

        choice = input("Обери дію: ")

        if choice == "1":
            print_diary(diary)

        elif choice == "2":
            add_entry(diary)

        elif choice == "3":
            search_entries(diary)

        elif choice == "4":
            print("До наступної подорожі!")
            break

        else:
            print("Невірний вибір. Спробуй ще раз.")


if __name__ == "__main__":
    main()
