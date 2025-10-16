import util_plant
import util_move

def plant_carrot(x, y, x_size, y_size):

    def do_planting(x, y):
        util_plant.do_planting(Entities.Carrot, True)

    util_move.move_to_and_zig_zag(x, y, x_size, y_size, do_planting)