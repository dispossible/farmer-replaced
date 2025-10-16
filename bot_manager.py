import util_upgrade
import util_spawn_drone

from plant_grass import plant_grass
from plant_trees import plant_trees
from plant_carrot import plant_carrot
from plant_pumpkin import plant_pumpkin
from plant_sunflowers import plant_sunflowers_sort
from plant_cacti import plant_cacti
from plant_maze import plant_maze


def bot():
    
    def drone_func_0():
        plant_grass(0, 0, 6, 6, True)
    util_spawn_drone.create_drone(drone_func_0)
    
    def drone_func_1():
        plant_trees(6, 0, 6, 6, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_1)

    def drone_func_3():
        plant_carrot(12, 0, 6, 6)
    util_spawn_drone.create_drone(drone_func_3)

    def drone_func_4():
        plant_pumpkin(0, 6, 6)
    util_spawn_drone.create_drone(drone_func_4)

    def drone_func_5():
        plant_sunflowers_sort(6, 6, 6, 6)
    util_spawn_drone.create_drone(drone_func_5)

    def drone_func_6():
        plant_cacti(12, 6, 6, 6)
    util_spawn_drone.create_drone(drone_func_6)

    def drone_func_7():
        plant_maze(0, 12, 10)
    util_spawn_drone.create_drone(drone_func_7)

    def drone_func_8():
        plant_pumpkin(10, 12, 8)
    util_spawn_drone.create_drone(drone_func_8)

    def drone_func_9():
        plant_cacti(18, 12, 4, 10)
    util_spawn_drone.create_drone(drone_func_9)

    def drone_func_10():
        plant_trees(18, 0, 4, 12, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_10)

    def drone_func_11():
        plant_grass(10, 20, 8, 2, False)
    util_spawn_drone.create_drone(drone_func_11)

    while True:
        util_upgrade.buy_upgrades()


    
if __name__ == "__main__":
    clear()
    bot()