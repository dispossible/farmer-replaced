import util_move
import util_plant

def plant_trees(x, y, x_size, y_size, alt_crop):

    def plant_tree(x, y):
        if can_harvest():
            harvest()

        if get_pos_y() % 2 != get_pos_x() % 2:
            util_plant.do_planting(Entities.Tree, True)
        else:
            util_plant.do_planting(alt_crop, True)

    util_move.move_to_and_zig_zag(x, y, x_size, y_size, plant_tree)