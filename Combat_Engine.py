class Combat_Engine:

    def combat(self, player, enemy, first_strike):
        PLAYER_STRIKE = 0

        if first_strike == PLAYER_STRIKE:
            print(f'{player.get_name()} attacks {enemy.get_name()} for {player.get_attack()} damage!')
            enemy.health_loss(player.get_attack())





