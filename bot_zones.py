import util_upgrade

from plant_pumpkin import plant_pumpkin
from plant_sunflowers import plant_sunflowers_sort
from plant_trees import plant_trees
from plant_cacti import plant_cacti
from plant_maze import plant_maze
from plant_carrot import plant_carrot
from plant_grass import plant_grass

def bot():
    while True:
        util_upgrade.buy_upgrades()

        plant_cacti(12, 0, 4, 8)
        plant_pumpkin(16, 0, 6)
        plant_carrot(0, 0, 6, 4)
        plant_sunflowers_sort(6, 0, 6, 4)
        plant_trees(0, 4, 4, 8, Entities.Bush)
        plant_trees(16, 6, 6, 8, Entities.Bush)
        plant_pumpkin(4, 4, 8)
        plant_grass(12, 8, 4, 4, False)
        plant_grass(0, 12, 8, 4, True)
        plant_carrot(8, 12, 8, 4)



if __name__ == "__main__":
    bot()