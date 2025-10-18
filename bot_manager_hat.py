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
    
    def drone_func_0():
        plant_grass(0, 0, 8, 8, False)
    util_spawn_drone.create_drone(drone_func_0, None, Hats.Straw_Hat)
    
    def drone_func_1():
        plant_trees(8, 0, 8, 8, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_1, None, Hats.Tree_Hat)
    
    def drone_func_2():
        plant_carrot(0, 8, 8, 8)
    util_spawn_drone.create_drone(drone_func_2, None, Hats.Carrot_Hat)
    
    def drone_func_3():
        plant_cacti(8, 8, 8, 8)
    util_spawn_drone.create_drone(drone_func_3, None, Hats.Cactus_Hat)
    
    def drone_func_4():
        plant_cacti(16, 0, 8, 8)
    util_spawn_drone.create_drone(drone_func_4, None, Hats.Cactus_Hat)
    
    def drone_func_5():
        plant_trees(24, 0, 8, 8, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_5, None, Hats.Tree_Hat)
    
    def drone_func_6():
        plant_carrot(16, 8, 8, 8)
    util_spawn_drone.create_drone(drone_func_6, None, Hats.Carrot_Hat)
    
    def drone_func_7():
        plant_cacti(24, 8, 8, 8)
    util_spawn_drone.create_drone(drone_func_7, None, Hats.Cactus_Hat)
    
    def drone_func_8():
        plant_maze(0, 16, 16)
    util_spawn_drone.create_drone(drone_func_8, None, Hats.Traffic_Cone)
    
    def drone_func_9():
        plant_cacti(16, 16, 8, 8)
    util_spawn_drone.create_drone(drone_func_9, None, Hats.Cactus_Hat)
    
    def drone_func_10():
        plant_cacti(24, 24, 8, 8)
    util_spawn_drone.create_drone(drone_func_10, None, Hats.Cactus_Hat)
    
    def drone_func_11():
        plant_sunflowers_force(16, 24, 8, 8)
    util_spawn_drone.create_drone(drone_func_11, None, Hats.Sunflower_Hat)
    
    def drone_func_12():
        plant_sunflowers_force(24, 16, 8, 8)
    util_spawn_drone.create_drone(drone_func_12, None, Hats.Sunflower_Hat)
    
    while True:
        util_upgrade.buy_upgrades()
        do_a_flip()


    
if __name__ == "__main__":
    clear()
    bot()