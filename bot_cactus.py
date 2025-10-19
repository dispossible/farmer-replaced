import util_upgrade

from plant_cacti import plant_cacti, plant_cacti_focus

def bot():
    clear()
    
    while True:
        util_upgrade.buy_upgrades()

        # plant_cacti(0, 0, get_world_size(), get_world_size())
        plant_cacti_focus(0, 0, get_world_size(), get_world_size())


    
if __name__ == "__main__":
    bot()