import util_move
import util_plant
import util_upgrade

from plant_pumpkin import plant_pumpkin
from plant_sunflowers import plant_sunflowers, plant_sunflowers_sort
from plant_trees import plant_trees
from plant_cacti import plant_cacti
from plant_maze import plant_maze

def bot():
    while True:

        util_upgrade.buy_upgrades()


        plant_cacti(12, 0, 4, 8)

        
        plant_pumpkin(16, 0, 6)


        def plant_carrot(x, y):
            util_plant.do_planting(Entities.Carrot, True)
        util_move.move_to_and_zig_zag(0, 0, 6, 4, plant_carrot)


        plant_sunflowers_sort(6, 0, 6, 4)


        plant_trees(0, 4, 4, 8, Entities.Bush)

        plant_trees(16, 6, 6, 8, Entities.Bush)


        plant_pumpkin(4, 4, 8)


        def plant_grass(x, y):
            util_plant.do_planting(Entities.Grass, True)
        util_move.move_to_and_zig_zag(12, 8, 4, 4, plant_grass)


        def plant_fertile_grass(x, y):
            util_plant.do_planting(Entities.Grass, True, True)
        util_move.move_to_and_zig_zag(0, 12, 8, 4, plant_fertile_grass)

        
        util_move.move_to_and_zig_zag(8, 12, 8, 4, plant_carrot)



if __name__ == "__main__":
    bot()