import json
import os

class WeaponEditor:
    def __init__(self, filename="weapons_db.json"):
        self.filename = filename
        self.weapons = self.load_data()

    def load_data(self):
        """Загрузка данных из файла (Read)"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_data(self):
        """Сохранение данных в файл (Create/Update)"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.weapons, f, indent=4, ensure_ascii=False)
        print("[Файл] Данные успешно синхронизированы с базой.")

    def add_weapon(self, name, damage, fire_rate):
        """Добавление нового оружия (Create)"""
        self.weapons[name] = {
            "damage": damage,
            "fire_rate": fire_rate,
            "dps": damage * fire_rate
        }
        print(f"[Редактор] Оружие '{name}' добавлено.")
        self.save_data()

    def delete_weapon(self, name):
        """Удаление оружия (Delete)"""
        if name in self.weapons:
            del self.weapons[name]
            print(f"[Редактор] Оружие '{name}' удалено.")
            self.save_data()
        else:
            print("[Ошибка] Оружие не найдено.")

# Демонстрация работы редактора
editor = WeaponEditor()

print("\n--- Запуск модуля Редактор Оружия ---")
# 1. Создаем (Create)
editor.add_weapon("Плазменная винтовка", damage=45, fire_rate=1.5)
editor.add_weapon("Лазерный пистолет", damage=15, fire_rate=5.0)

# 2. Читаем (Read)
print(f"Текущий арсенал: {list(editor.weapons.keys())}")

# 3. Обновляем (Update - просто повторный вызов с тем же именем)
editor.add_weapon("Лазерный пистолет", damage=20, fire_rate=5.0)

# 4. Удаляем (Delete)
# editor.delete_weapon("Плазменная винтовка")
