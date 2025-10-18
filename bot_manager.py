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
        plant_grass(0, 0, 6, 6, True)
    util_spawn_drone.create_drone(drone_func_0, None, Hats.Straw_Hat)
    
    def drone_func_1():
        plant_trees(6, 0, 6, 6, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_1, None, Hats.Tree_Hat)

    def drone_func_3():
        plant_carrot(12, 0, 6, 6)
    util_spawn_drone.create_drone(drone_func_3, None, Hats.Carrot_Hat)

    def drone_func_4():
        plant_pumpkin(0, 6, 6)
    util_spawn_drone.create_drone(drone_func_4, None, Hats.Gold_Hat)

    def drone_func_5():
        plant_sunflowers_force(6, 6, 6, 6)
    util_spawn_drone.create_drone(drone_func_5, None, Hats.Sunflower_Hat)

    def drone_func_6():
        plant_cacti(12, 6, 6, 6)
    util_spawn_drone.create_drone(drone_func_6, None, Hats.Cactus_Hat)

    def drone_func_7():
        plant_maze(0, 18, 12)
    util_spawn_drone.create_drone(drone_func_7, None, Hats.Traffic_Cone)

    def drone_func_8():
        plant_pumpkin(12, 12, 6)
    util_spawn_drone.create_drone(drone_func_8, None, Hats.Gold_Hat)

    def drone_func_9():
        plant_cacti(18, 12, 6, 6)
    util_spawn_drone.create_drone(drone_func_9, None, Hats.Cactus_Hat)

    def drone_func_10():
        plant_trees(18, 0, 6, 6, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_10, None, Hats.Tree_Hat)

    def drone_func_11():
        plant_grass(18, 6, 6, 6, False)
    util_spawn_drone.create_drone(drone_func_11, None, Hats.Straw_Hat)

    def drone_func_12():
        plant_carrot(12, 18, 6, 6)
    util_spawn_drone.create_drone(drone_func_12, None, Hats.Carrot_Hat)

    def drone_func_13():
        plant_trees(18, 18, 6, 6, Entities.Bush)
    util_spawn_drone.create_drone(drone_func_13, None, Hats.Tree_Hat)

    def drone_func_14():
        plant_carrot(24, 0, 6, 6)
    util_spawn_drone.create_drone(drone_func_14, None, Hats.Carrot_Hat)

    def drone_func_15():
        plant_sunflowers_force(24, 6, 6, 6)
    util_spawn_drone.create_drone(drone_func_15, None, Hats.Sunflower_Hat)

    def drone_func_16():
        plant_pumpkin(24, 12, 6)
    util_spawn_drone.create_drone(drone_func_16, None, Hats.Gold_Hat)

    def drone_func_17():
        plant_cacti(24, 18, 6, 6)
    util_spawn_drone.create_drone(drone_func_17, None, Hats.Cactus_Hat)

    def drone_func_18():
        plant_grass(24, 24, 6, 6, False)
    util_spawn_drone.create_drone(drone_func_18, None, Hats.Straw_Hat)

    def drone_func_19():
        plant_carrot(18, 24, 6, 6)
    util_spawn_drone.create_drone(drone_func_19, None, Hats.Carrot_Hat)
    
    def drone_func_20():
        plant_carrot(6, 12, 6, 6)
    util_spawn_drone.create_drone(drone_func_20, None, Hats.Carrot_Hat)

    def drone_func_21():
        plant_grass(12, 24, 6, 6, True)
    util_spawn_drone.create_drone(drone_func_21, None, Hats.Straw_Hat)

    def drone_func_22():
        plant_cacti(0, 12, 6, 6)
    util_spawn_drone.create_drone(drone_func_22, None, Hats.Cactus_Hat)

    def drone_func_23():
        plant_sunflowers_force(0, 30, 32, 2)
    util_spawn_drone.create_drone(drone_func_23, None, Hats.Sunflower_Hat)

    def drone_func_24():
        plant_sunflowers_force(30, 0, 2, 30)
    util_spawn_drone.create_drone(drone_func_24, None, Hats.Sunflower_Hat)
    
    while True:
        util_upgrade.buy_upgrades()
        do_a_flip()


    
if __name__ == "__main__":
    clear()
    bot()