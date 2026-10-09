class Character:
    def __init__(self, name, strength=10, hp=100, damage=5):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.max_hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} получает {amount} урона. HP: {self.hp}/{self.max_hp}")

    def attack(self, target):
        dealt = self.damage + self.strength // 2
        print(f"{self.name} атакует {target.name} на {dealt} урона!")
        target.take_damage(dealt)

    def show_stats(self):
        print(f"[{self.name}] Сила: {self.strength}, HP: {self.hp}/{self.max_hp}, Урон: {self.damage}")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"  {self.name} восстанавливает {amount} HP. HP:{self.hp}/{self.max_hp}")

ENEMY_TYPES = [
    {"name": "Гоблин",           "strength": 6,  "hp": 60,  "damage": 4},
    {"name": "Разбойник",        "strength": 10, "hp": 100, "damage": 7},
    {"name": "Глава разбойников","strength": 14, "hp": 140, "damage": 11},
    {"name": "Вампир",           "strength": 20, "hp": 140, "damage": 15},
    {"name": "Лорд Вампиров",    "strength": 30, "hp": 160, "damage": 20},
]

def spawn_enemy(wave):
    base = ENEMY_TYPES[min(wave - 1, len(ENEMY_TYPES)-1)]
    scale = 1 + 0.15 * (wave - 1)
    return Character(
        name=f"f{base['name']} (волна {wave})",
        strength = int(base["strength"]*scale),
        hp = int(base["hp"] * scale),
        damage = int(base["damage"]*scale),
    )



player = Character("Темный Соблазн", strength=12, hp=120, damage=8)
wave = 1

player.show_stats()

while player.is_alive():
    enemy = spawn_enemy(wave)
    print(f"\n-- ВОЛНА {wave} ---")
    enemy.show_stats()

    while player.is_alive() and enemy.is_alive():
        input("\nНажми Enter для атаки...")
        player.attack(enemy)
        if not enemy.is_alive():
            print(f"\n{enemy.name} повержен! Победа!")
            break
        enemy.attack(player)
        if not player.is_alive():
            print(f"\n{player.name} погиб... Игра окончена.")
            break

    if not player.is_alive():
                break
    wave +=1
    print(f"\n=== Волна {wave - 1} пройдена! ===")
    player.heal(player.max_hp // 4)