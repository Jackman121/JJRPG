class Character:
    def __init__(self, name, health, mana, attack):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack

    def __str__(self):
        return f"Name:{self.name}, Hp:{self.health}, Mana:{self.mana}"

    def health_loss(self, health_lost):
        self.health = self.health - health_lost
        if self.health < 0:
            self.health = 0

    def get_health(self):
        return f'{self.health}'

    def get_attack(self):
        return self.attack

    def get_name(self):
        return self.name


class Player(Character):

    def playerSpecificAttack(self):
        print("Player attack")


class NPC(Character):

    def NPCSpecificAttack(self):
        print("NPC attack")
