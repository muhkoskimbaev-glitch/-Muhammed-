import re
import os

WIDTH = 60  # ширина рамки


def clear():
    """Очищает консоль."""
    os.system("cls" if os.name == "nt" else "clear")


def line(char="─"):
    """Печатает горизонтальный разделитель."""
    print(char * WIDTH)


def title(text: str):
    """Печатает заголовок в рамке."""
    line("═")
    print(f"  {text.upper()}")
    line("═")


def box(text: str):
    """Печатает текст в простой рамке из ─."""
    line()
    for row in text.strip().split("\n"):
        print(f"  {row}")
    line()


def validate_input(choice: str) -> bool:
    """Проверяет что ввод — целое число через regex."""
    return bool(re.fullmatch(r"\d+", choice.strip()))


def pause():
    """Ожидает нажатия Enter."""
    print()
    input("  Нажмите Enter для продолжения...")
