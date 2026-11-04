import util_upgrade
import util_plant
import util_move

from plant_grass import plant_grass
from plant_trees import plant_trees, plant_bushes
from plant_carrot import plant_carrot
from plant_pumpkin import plant_pumpkin, plant_pumpkin_focus
from plant_cacti import plant_cacti
from plant_maze import plant_maze

def bot():
    clear()
    early_game()

    while True:
        world_size = get_world_size()

        crops_needed = util_upgrade.get_crop_requirements()
        field_size = 2

        if world_size == 6:
            field_size = 3
        if world_size == 8:
            field_size = 4
        if world_size == 12:
            field_size = 3
        if world_size == 16:
            field_size = 4

        farm_fields(crops_needed, world_size, field_size)

        if world_size < 6:
            util_upgrade.buy_upgrades(0)
        else:
            util_upgrade.buy_upgrades()
                

def early_game():
    farm_single_hay(20)
    unlock(Unlocks.Speed)
    farm_single_hay(30)
    unlock(Unlocks.Expand)
    farm_triple(Entities.Grass, Items.Hay, 50)
    unlock(Unlocks.Plant)
    farm_triple(Entities.Bush, Items.Wood, 20)
    unlock(Unlocks.Expand)
    farm_nine_a()
    unlock(Unlocks.Carrots)
    farm_nine_b()
    unlock(Unlocks.Expand)


# Earily game, hammer out hay
def farm_single_hay(amount = 10):
    for i in range(amount):
        while not can_harvest():
            pass
        harvest()


# Earily game triple, all wood
def farm_triple(crop, item, amount):
    while num_items(item) < amount:
        util_plant.do_planting(crop, True)
        move(North)
        util_plant.do_planting(crop, True)
        move(North)
        util_plant.do_planting(crop, True)
        move(North)


def simple_plant_bush(x, y):
    util_plant.do_planting(Entities.Bush, True)

def simple_plant_grass(x, y):
    util_plant.do_planting(Entities.Grass, True)

def simple_plant_carrot(x, y):
    util_plant.do_planting(Entities.Carrot, True)

def farm_nine_a(amount = 50):
    while num_items(Items.Wood) < amount:
        util_move.move_to_and_zig_zag(0, 0, 3, 3, simple_plant_bush)

def farm_nine_b(amount_wood = 30, amount_carrot = 20):
    while num_items(Items.Wood) < amount_wood or num_items(Items.Carrot) < amount_carrot:
        util_move.move_to_and_zig_zag(0, 0, 2, 2, simple_plant_bush)
        util_move.move_to_and_zig_zag(2, 0, 1, 2, simple_plant_grass)
        util_move.move_to_and_zig_zag(0, 2, 3, 1, simple_plant_carrot)

def farm_fields(crops, world_size, field_size):
        i = 0
        for x in range(0, world_size, field_size):
            for y in range(0, world_size, field_size):
                crop = crops[i % len(crops)]

                if crop == Entities.Grass:
                    plant_grass(x, y, field_size, field_size)
                elif crop == Entities.Bush:
                    plant_bushes(x, y, field_size, field_size)
                elif crop == Entities.Tree:
                    plant_trees(x, y, field_size, field_size, Entities.Bush)
                elif crop == Entities.Carrot:
                    plant_carrot(x, y, field_size, field_size)
                elif crop == Entities.Pumpkin:
                    plant_pumpkin(x, y, field_size)
                elif crop == Entities.Cactus:
                    plant_cacti(x, y, field_size, field_size)
                elif crop == Items.Weird_Substance:
                    plant_grass(x, y, field_size, field_size, True)
                elif crop == Items.Gold:
                    plant_maze(x, y, field_size)

                i += 1



if __name__ == "__main__":
    bot()
