def attack(player, enemies):
    if not enemies:
        print("Keine Gegner zum angreifen.")
    else:
        for enemy in enemies:
            player.attack(enemy)
            if enemy.is_dead:
                enemies.remove(enemy)
            print("")
            enemy.attack(player)
            if player.is_dead:
                print("Du bist leider gestorben, viel Glück beim nächsten mal.")
                exit()
