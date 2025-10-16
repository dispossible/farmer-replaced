import util_plant
import util_move

def plant_grass(x, y, x_size, y_size, fertilize=False):

    def do_planting(x, y):
        util_plant.do_planting(Entities.Grass, True, fertilize)

    util_move.move_to_and_zig_zag(x, y, x_size, y_size, do_planting)