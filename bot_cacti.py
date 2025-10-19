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
    
    def create_drone(x, y, size):
        
        def drone_func_cacti():
            plant_cacti(x, y, size, size)
        
        def drone_func_carrot():
            plant_carrot(x, y, size, size)

        if x % 2 != y % 2:
            util_spawn_drone.create_drone(drone_func_cacti, None, Hats.Cactus_Hat)
        

    util_spawn_drone.create_drone_grid(create_drone, 6)
    
    while True:
        util_upgrade.buy_upgrades()
        do_a_flip()


    
if __name__ == "__main__":
    clear()
    bot()