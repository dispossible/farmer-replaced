import util_move
import util_plant

pumpkin_ready = {}
def plant_pumpkin(x, y, size):
    pumpkin_id = str(x) + "," + str(y)
    pumpkin_ready[pumpkin_id] = True

    def check_pumpkin(x, y):
        util_plant.do_planting(Entities.Pumpkin)
        if not can_harvest():
            pumpkin_ready[pumpkin_id] = False

    util_move.move_to_and_zig_zag(x, y, size, size, check_pumpkin)

    if pumpkin_ready[pumpkin_id]:
        harvest()
        plant_pumpkin(x, y, size)


def plant_pumpkin_focus(x, y, size):
    queue = []
    for qx in range(size):
        for qy in range(size):
            if qx % 2 == 0:
                queue.append((qx, qy))
            else:
                queue.append((qx, size - qy - 1))

    while len(queue) > 0:
        next_queue = []
        for pos in queue:
            util_move.move_to(x + pos[0], y + pos[1])
            util_plant.do_planting(Entities.Pumpkin)
            if not can_harvest():
                next_queue.append(pos)
        queue = next_queue

    harvest()