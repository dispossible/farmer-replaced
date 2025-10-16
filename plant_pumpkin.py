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