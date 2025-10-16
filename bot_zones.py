import util_move
import util_plant

from plant_pumpkin import plant_pumpkin
from plant_sunflowers import plant_sunflowers
from plant_trees import plant_trees
from plant_cacti import plant_cacti

def zones():
    while True:

        plant_cacti(12, 0, 4, 8)


        def plant_carrot(x, y):
            util_plant.do_planting(Entities.Carrot, True)
        util_move.move_to_and_zig_zag(0, 0, 6, 4, plant_carrot)


        plant_sunflowers(8, 0, 4, 4)


        plant_trees(0, 4, 4, 4, Entities.Bush)


        plant_pumpkin(4, 4, 8)


        def plant_grass(x, y):
            util_plant.do_planting(Entities.Grass, True)
        util_move.move_to_and_zig_zag(0, 8, 4, 4, plant_grass)