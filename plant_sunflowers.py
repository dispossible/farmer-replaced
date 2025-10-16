import util_move
import util_plant

def plant_sunflowers(x, y, x_size, y_size):
    change_hat(Hats.Sunflower_Hat)

    def check_sunflowers(x, y):
        if get_entity_type() != Entities.Sunflower:
            util_plant.do_planting(Entities.Sunflower)
        while measure() < 15:
            harvest()
            plant(Entities.Sunflower)

    util_move.move_to_and_zig_zag(x, y, x_size, y_size, check_sunflowers)

    count = [(x_size * y_size) - 9]
    def harvest_sunflower(x, y):
        if count[0] > 0 and can_harvest():
            harvest()
            count[0] -= 1

    util_move.move_to_and_zig_zag(x, y, x_size, y_size, harvest_sunflower)

    change_hat(Hats.Straw_Hat)