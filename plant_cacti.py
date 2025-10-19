import util_move
import util_plant
import util_spawn_drone

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

# ----------------------------

def plant_cacti_focus(x, y, x_size, y_size):

    # Plant a column
    def drone_planter():
        for py in range(y, y + y_size):
            util_plant.do_planting(Entities.Cactus)
            move(North)

    for px in range(x, x + x_size - 1):
        util_move.move_to(px, y)

        # Wait if there are no drones available
        while max_drones() == num_drones():
            pass

        util_spawn_drone.create_drone(drone_planter, 1, Hats.Cactus_Hat)

    util_move.move_to(x + x_size - 1, y)
    drone_planter()

    # all squares are planeted
    sort_cacti(x, y, x_size, y_size)


def sort_cacti(x, y, x_size, y_size):
    w = x
    s = y
    e = x + x_size - 1
    n = y + y_size - 1
    
    util_move.move_to(x, y)

    def sort_dir(dir):
        size = measure()
        next_size = measure(dir)
        if size > next_size and (dir == East or dir == North):
            swap(dir)
            return True
        elif size < next_size and (dir == West or dir == South):
            swap(dir)
            return True
        else:
            return False

    def drone_sorter_vertical():
        has_swapped = [True]

        def sort_cactus_vertical():
            swapped = False
            if(get_pos_y() < n):
                swapped = swapped or sort_dir(North)
            if(get_pos_y() > s):
                swapped = swapped or sort_dir(South)
            if swapped:
                has_swapped[0] = True

        while has_swapped[0]:
            has_swapped = [False]
            util_move.move_to(get_pos_x(), y)
            for py in range(y, y + y_size):
                sort_cactus_vertical()
                move(North)
    
    for px in range(x, x + x_size - 1):
        util_move.move_to(px, y)

        # Wait if there are no drones available
        while max_drones() == num_drones():
            pass

        util_spawn_drone.create_drone(drone_sorter_vertical, 1, Hats.Wizard_Hat)
    
    util_move.move_to(x + x_size - 1, y)
    drone_sorter_vertical()

    # Wait for the sorters to finish
    while num_drones() > 1:
        pass

    def drone_sorter_horizontal():
        has_swapped = [True]

        def sort_cactus_horizontal():
            swapped = False
            if(get_pos_x() < e):
                swapped = swapped or sort_dir(East)
            if(get_pos_x() > w):
                swapped = swapped or sort_dir(West)
            if swapped:
                has_swapped[0] = True

        while has_swapped[0]:
            has_swapped = [False]
            util_move.move_to(x, get_pos_y())
            for px in range(x, x + x_size):
                sort_cactus_horizontal()
                move(East)
                
    for py in range(y, y + y_size - 1):
        util_move.move_to(x, py)

        # Wait if there are no drones available
        while max_drones() == num_drones():
            pass

        util_spawn_drone.create_drone(drone_sorter_horizontal, 1, Hats.Wizard_Hat)
    
    util_move.move_to(x, y + y_size - 1)
    drone_sorter_horizontal()

    # Wait for the sorters to finish
    while num_drones() > 1:
        pass

    harvest()