import util_move
import util_plant

cacti_ready = {}
cacti_sort_updated = {}
def plant_cacti(x, y, x_size, y_size):

    cacti_id = str(x) + "," + str(y)
    cacti_ready[cacti_id] = True
    cacti_sort_updated[cacti_id] = True

    def check_cacti(x, y):
        util_plant.do_planting(Entities.Cactus)
        if not can_harvest():
            cacti_ready[cacti_id] = False

    util_move.move_to_and_zig_zag(x, y, x_size, y_size, check_cacti)


    if cacti_ready[cacti_id]:
        # Do the sorting
        w = x
        s = y
        e = x + x_size - 1
        n = y + y_size - 1

        def sort_dir(dir):
            size = measure()
            next_size = measure(dir)
            if size > next_size and (dir == East or dir == North):
                swap(dir)
                cacti_sort_updated[cacti_id] = True
            elif size < next_size and (dir == West or dir == South):
                swap(dir)
                cacti_sort_updated[cacti_id] = True

        def sort_cactus(x, y):
            if(get_pos_x() < e):
                sort_dir(East)
            if(get_pos_y() < n):
                sort_dir(North)
            if(get_pos_x() > w):
                sort_dir(West)
            if(get_pos_y() > s):
                sort_dir(South)

        while cacti_sort_updated[cacti_id]:
            cacti_sort_updated[cacti_id] = False
            util_move.move_to_and_zig_zag(x, y, x_size, y_size, sort_cactus)

        harvest()
        util_move.move_to_and_zig_zag(x, y, x_size, y_size, check_cacti)

