
def create_drone(drone_func, ttl = None, hat = Hats.Brown_Hat):
    def inner_func():
        change_hat(hat)
        if ttl != None:
            for _ in range(ttl):
                drone_func()
        else:
            while True:
                drone_func()
                
    return spawn_drone(inner_func)


def create_drone_grid(create_drone_func, grid_size, ttl = None, hat = Hats.Brown_Hat):
    tile_size = get_world_size() // grid_size

    for x in range(grid_size):
        for y in range(grid_size):
            create_drone_func(x * tile_size, y * tile_size, tile_size)