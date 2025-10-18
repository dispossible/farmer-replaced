import util_upgrade

from plant_pumpkin import plant_pumpkin_focus

def bot():
    clear()
    while True:
        util_upgrade.buy_upgrades()

        plant_pumpkin_focus(0, 0, 32)



if __name__ == "__main__":
    bot()