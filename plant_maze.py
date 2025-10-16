
import util_move
import util_plant
import util_math
import util_list

def plant_maze(x, y, size, solve = True):
    substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
    center = util_math.floor(size / 2)

    util_move.move_to(x + center, y + center)
    util_plant.do_planting(Entities.Bush)
    use_item(Items.Weird_Substance, substance)

    if solve:
        solve_maze()


directions = [
    (North, 0, 1),
    (East, 1, 0),
    (South, 0, -1),
    (West, -1, 0)
]

def solve_maze():
    target_x, target_y = measure()

    world_size = get_world_size()
    visited = util_list.array_2d(world_size, world_size, False)
    path = []

    def distance_between(x1, y1, x2, y2):
        dx = min(abs(x1 - x2), world_size - abs(x1 - x2))
        dy = min(abs(y1 - y2), world_size - abs(y1 - y2))
        return dx + dy

    def depth_first_search(x, y):
        if (x, y) == (target_x, target_y):
            return True

        visited[x][y] = True

        # Manually order directions by distance to target
        dir_dist = []
        for dir, dx, dy in directions:
            next_x = (x + dx) % world_size
            next_y = (y + dy) % world_size
            dist = distance_between(next_x, next_y, target_x, target_y)
            dir_dist.append((dist, dir, dx, dy))

        def sort(a, b):
            return a[0] >= b[0]
        util_list.sort_list(dir_dist, sort)

        for _, dir, dx, dy in dir_dist:
            next_x = (x + dx) % world_size
            next_y = (y + dy) % world_size

            if not visited[next_x][next_y]:
                if move(dir):
                    path.append(dir)
                    if depth_first_search(next_x, next_y):
                        return True
                    # backtrack
                    if dir == North:
                        move(South)
                    elif dir == South:
                        move(North)
                    elif dir == East:
                        move(West)
                    elif dir == West:
                        move(East)
                    path.pop()
        return False

    depth_first_search(get_pos_x(), get_pos_y())

    harvest()
