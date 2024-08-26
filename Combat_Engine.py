class Combat_Engine:

    def combat(self, player, enemy, first_strike):
        PLAYER_STRIKE = 0

        if first_strike == PLAYER_STRIKE:
            enemy.health_loss(player.get_attack())





