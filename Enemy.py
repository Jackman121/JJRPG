class Enemy:
    def __init__(self, name, health, mana, attack):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack

    def __str__(self):
        return f"Name:{self.name}, Hp:{self.health}, Mana:{self.mana}"

    def health_loss(self, health_lost):
        self.health = self.health - health_lost

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
