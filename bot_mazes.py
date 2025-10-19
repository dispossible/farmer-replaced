import util_upgrade
import util_spawn_drone

from plant_grass import plant_grass
from plant_trees import plant_trees
from plant_carrot import plant_carrot
from plant_pumpkin import plant_pumpkin
from plant_sunflowers import plant_sunflowers_force
from plant_cacti import plant_cacti
from plant_maze import plant_maze


def bot():
    change_hat(Hats.The_Farmers_Remains)
    
    def make_drone(x, y, size):
        def drone_func_0():
            plant_maze(x, y, size, size)
        util_spawn_drone.create_drone(drone_func_0, None, Hats.Traffic_Cone)

    util_spawn_drone.create_drone_grid(make_drone, 4)

    
    while True:
        util_upgrade.buy_upgrades()
        do_a_flip()


    
if __name__ == "__main__":
    clear()
    bot()