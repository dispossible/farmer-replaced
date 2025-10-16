import util_upgrade

from plant_maze import plant_maze, solve_maze

def bot():
    while True:
        util_upgrade.buy_upgrades()

        plant_maze(0, 0, get_world_size())

    
if __name__ == "__main__":
    bot()