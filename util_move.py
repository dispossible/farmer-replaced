def move_times(dir, times):
    for x in range(times):
        move(dir)

def noop(x, y):
    pass

def move_to(x, y, cb = noop):
    world_size = get_world_size()

    # Get current position
    current_x = get_pos_x()
    current_y = get_pos_y()

    # Calculate distance to target
    distance_east = (x - current_x) % world_size
    distance_west = (current_x - x) % world_size
    distance_north = (y - current_y) % world_size
    distance_south = (current_y - y) % world_size

    # Determine shortest directions
    direction_x = East 
    if distance_east > distance_west:
        direction_x = West

    direction_y = North
    if distance_north > distance_south:
        direction_y = South

    # Move horizontally
    while get_pos_x() != x:
        move(direction_x)
        cb(None, None)

    # Move vertically
    while get_pos_y() != y:
        move(direction_y)
        cb(None, None)


def move_to_nowrap(x, y, cb = noop):
    # Get current position
    current_x = get_pos_x()
    current_y = get_pos_y()

    # Calculate distance to target
    distance_x = (x - current_x)
    distance_y = (y - current_y)

    # Determine directions
    direction_x = East 
    if distance_x < 0:
        direction_x = West

    direction_y = North
    if distance_y < 0:
        direction_y = South

    # Move horizontally
    while get_pos_x() != x:
        move(direction_x)
        cb(None, None)

    # Move vertically
    while get_pos_y() != y:
        move(direction_y)
        cb(None, None)


def move_zig_zag(x_size, y_size, x_dir, y_dir, cb = noop):
    for x in range(x_size):
        for y in range(y_size):
            cb(x, y)
            
            if y < y_size - 1:
                zig_y_dir = y_dir
                if x % 2 == 1:
                    if y_dir == North:
                        zig_y_dir = South
                    else:
                        zig_y_dir = North
                move(zig_y_dir)
        if x < x_size - 1:
            move(x_dir)


def distance_to(x, y):
    world_size = get_world_size()

    # Get current position
    current_x = get_pos_x()
    current_y = get_pos_y()

    # Calculate distance to target
    distance_east = (x - current_x) % world_size
    distance_west = (current_x - x) % world_size
    distance_north = (y - current_y) % world_size
    distance_south = (current_y - y) % world_size

    return min(distance_east, distance_west) + min(distance_north, distance_south)


def move_to_and_zig_zag(x, y, x_size, y_size, cb = noop):
    w = x
    e = x + x_size - 1
    s = y
    n = y + y_size - 1

    sw_distance = distance_to(w, s)
    se_distance = distance_to(e, s)
    nw_distance = distance_to(w, n)
    ne_distance = distance_to(e, n)

    min_distance = min(sw_distance, se_distance, nw_distance, ne_distance)

    if sw_distance <= min_distance:
        move_to(w, s)
        move_zig_zag(x_size, y_size, East, North, cb)

    elif se_distance <= min_distance:
        move_to(e, s)
        move_zig_zag(x_size, y_size, West, North, cb)

    elif nw_distance <= min_distance:
        move_to(w, n)
        move_zig_zag(x_size, y_size, East, South, cb)

    else:
        move_to(e, n)
        move_zig_zag(x_size, y_size, West, South, cb)