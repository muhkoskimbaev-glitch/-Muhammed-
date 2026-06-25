import json
import os
from utils import title, line, box


class Portfolio:
    """Основной класс портфолио. Хранит данные и выводит разделы."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = self._load()

    # ── Загрузка данных ──────────────────────────────────────────────────────

    def _load(self) -> dict:
        """Загружает данные из JSON-файла."""
        if not os.path.exists(self.filepath):
            print(f"Файл '{self.filepath}' не найден!")
            return {}
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    # ── Универсальный вывод текстового блока ─────────────────────────────────

    def show(self, key: str, section_title: str):
        """Выводит текстовый раздел по ключу из data.json."""
        title(section_title)
        content = self.data.get(key, "Информация не найдена.")
        if isinstance(content, str):
            for row in content.strip().split("\n"):
                print(f"  {row}")
        else:
            print(f"  {content}")
        line()

    
    def show_progress(self):
        title("ТОЧКА А → ТОЧКА Б")
        progress = self.data.get("progress", {})

        print("  ТОЧКА А — С ЧЕГО Я НАЧИНАЛ:\n")
        for row in progress.get("point_a", "").split("\n"):
            print(f"    {row}")

        print()
        line("·")
        print()

        print("   ТОЧКА Б — ГДЕ Я СЕЙЧАС:\n")
        for row in progress.get("point_b", "").split("\n"):
            print(f"    {row}")

        line()

    

    def show_hobbies(self):
        title("ХОББИ И ИНТЕРЕСЫ")
        hobbies = self.data.get("hobbies", [])
        if not hobbies:
            print("  Информация не найдена.")
        else:
            for hobby in hobbies:
                print(f"  {hobby}")
        line()

    

    def show_works(self):
        title("МОИ ЛУЧШИЕ РАБОТЫ")
        works = self.data.get("works", [])
        if not works:
            print("  Работы не найдены.")
        else:
            for i, work in enumerate(works, 1):
                print(f"  {i}. {work.get('title', '—')}")
                print(f"      {work.get('description', '—')}")
                print(f"      {work.get('link', '—')}")
                if i < len(works):
                    print()
        line()

    

    def search(self, keyword: str):
        title(f"ПОИСК: «{keyword}»")
        keyword_lower = keyword.lower()
        found = False

        def scan(value, path=""):
            nonlocal found
            if isinstance(value, str):
                if keyword_lower in value.lower():
                    print(f"   [{path}]")
                    print(f"     ...{value.strip()[:120]}...")
                    print()
                    found = True
            elif isinstance(value, list):
                for item in value:
                    scan(item, path)
            elif isinstance(value, dict):
                for k, v in value.items():
                    scan(v, path=k if not path else f"{path} → {k}")

        scan(self.data)

        if not found:
            print(f"  Ничего не найдено по запросу «{keyword}»")
        line()
