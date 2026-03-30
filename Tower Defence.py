import math
import time

class Enemy:
    def __init__(self, name, health, speed, path):
        self.name = name
        self.health = health
        self.speed = speed
        self.path = path  # Список точек координат [(x, y), ...]
        self.current_point_idx = 0
        self.position = list(path[0])

    def move(self):
        """Реализация перемещения к следующей точке пути"""
        if self.current_point_idx < len(self.path) - 1:
            target = self.path[self.current_point_idx + 1]
            # Вычисление направления
            dx = target[0] - self.position[0]
            dy = target[1] - self.position[1]
            dist = math.sqrt(dx**2 + dy**2)

            if dist < 0.1:
                self.current_point_idx += 1
                print(f"[Система] {self.name} достиг точки {target}")
            else:
                # Плавное перемещение
                self.position[0] += (dx / dist) * self.speed
                self.position[1] += (dy / dist) * self.speed

class Tower:
    def __init__(self, range_radius, damage, fire_rate):
        self.range_radius = range_radius
        self.damage = damage
        self.fire_rate = fire_rate
        self.last_shot_time = 0

    def attack(self, enemy):
        """Логика проверки дистанции и стрельбы"""
        current_time = time.time()
        dist = math.sqrt((enemy.position[0])**2 + (enemy.position[1])**2)
        
        if dist <= self.range_radius:
            if current_time - self.last_shot_time >= 1 / self.fire_rate:
                enemy.health -= self.damage
                self.last_shot_time = current_time
                print(f"[Бой] Башня атакует {enemy.name}! Остаток HP: {max(0, enemy.health)}")

# Имитация игрового цикла
path_points = [(0, 0), (5, 5), (10, 0)]
virus = Enemy("Trojan.Win32", health=100, speed=0.5, path=path_points)
firewall = Tower(range_radius=7, damage=25, fire_rate=2)

print("--- Запуск модуля Tower Defense ---")
for _ in range(10):
    virus.move()
    firewall.attack(virus)
    if virus.health <= 0:
        print(f" Результат: {virus.name} уничтожен!")
        break
    time.sleep(0.2)
