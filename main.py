from portfolio import Portfolio
from utils import clear, line, title, validate_input, pause
from logger import log
from logo import draw_logo


MENU_ITEMS = {
    "1": "О себе",
    "2": "Моя цель",
    "3": "Как я пришёл в IT",
    "4": "Мой ментор",
    "5": "Точка А → Точка Б",
    "6": "Хобби и интересы",
    "7": "Мои лучшие работы",
    "8": "GitHub",
    "9": "Поиск по портфолио",
    "10": "Логотип (Turtle)",
    "0": "Выход",
}


def show_menu():
    clear()
    print()
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║              ПОРТФОЛИО «ОБО МНЕ»                    ║")
    print("  ║                Junior Python                         ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print()
    for key, label in MENU_ITEMS.items():
        if key == "0":
            line("─")
        print(f"    {key:>2}.  {label}")
    print()
    line("─")


def main():
    portfolio = Portfolio("data.json")
    log("Запуск программы")

    while True:
        show_menu()
        choice = input("  Выберите пункт: ").strip()

        # Разрешаем нечисловой ввод только для выхода (0)
        if choice == "0":
            clear()
            print()
            print("  До свидания! 👋")
            print()
            log("Выход из программы")
            break

        if not validate_input(choice):
            print("  Ошибка: введите число от 0 до 10.")
            pause()
            continue

        if choice not in MENU_ITEMS:
            print("  Нет такого пункта. Попробуйте ещё раз.")
            pause()
            continue

        log(f"Выбор пункта меню: {choice} — {MENU_ITEMS[choice]}")
        clear()
        print()

        if choice == "1":
            portfolio.show("about_me", "О СЕБЕ")

        elif choice == "2":
            portfolio.show("goal", "МОЯ ЦЕЛЬ")

        elif choice == "3":
            portfolio.show("it_story", "КАК Я ПРИШЁЛ В IT")

        elif choice == "4":
            portfolio.show("mentor", "МОЙ МЕНТОР")

        elif choice == "5":
            portfolio.show_progress()

        elif choice == "6":
            portfolio.show_hobbies()

        elif choice == "7":
            portfolio.show_works()

        elif choice == "8":
            portfolio.show("github", "GITHUB")

        elif choice == "9":
            print()
            keyword = input("  Введите слово для поиска: ").strip()
            if keyword:
                print()
                portfolio.search(keyword)
                log(f"Поиск: «{keyword}»")
            else:
                print("  Пустой запрос.")

        elif choice == "10":
            log("Запуск Turtle логотипа")
            draw_logo()

        pause()


if __name__ == "__main__":
    main()
