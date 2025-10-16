import util_upgrade

from plant_grass import plant_grass
from plant_trees import plant_trees
from plant_carrot import plant_carrot
from plant_pumpkin import plant_pumpkin
from plant_sunflowers import plant_sunflowers_sort
from plant_cacti import plant_cacti


def bot():
    
    def drone_func():
        plant_grass(0, 0, 6, 6, True)
    spawn_drone(drone_func)

    while True:
        util_upgrade.buy_upgrades()


    
if __name__ == "__main__":
    bot()