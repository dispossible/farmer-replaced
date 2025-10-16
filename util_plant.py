import util_water
import util_fertilize

needs_soil = {
    Entities.Carrot: True,
    Entities.Pumpkin: True,
    Entities.Sunflower: True,
    Entities.Cactus: True,
}

def do_planting(crop, do_harvest = False, apply_treatment = True):
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
        plant(crop)
    
    if apply_treatment:
        util_water.do_watering()
        # util_fertilize.do_fertilize()