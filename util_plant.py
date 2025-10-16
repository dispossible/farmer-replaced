import util_water
import util_fertilize

needs_soil = {
    Entities.Carrot: True,
    Entities.Pumpkin: True,
    Entities.Sunflower: True,
    Entities.Cactus: True,
}

def do_planting(crop, do_harvest = False, fertilize = False):
    if get_entity_type() != crop:
        harvest()

    if can_harvest() and do_harvest:
        harvest()

    if crop in needs_soil:
        if get_ground_type() != Grounds.Soil:
            till()
    else:
        if get_ground_type() == Grounds.Soil:
            till()

    if crop != Entities.Grass:
        costs = get_cost(crop)
        can_afford = True
        if costs:
            for needed_item in costs:
                owned = num_items(needed_item)
                if owned < costs[needed_item]:
                    can_afford = False
        if can_afford:
            plant(crop)
    
    util_water.do_watering()

    if fertilize:
        util_fertilize.do_fertilize()