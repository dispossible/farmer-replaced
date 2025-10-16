def stripfarm():
    while True:
        for x in range(get_world_size()):
            for y in range(get_world_size()):

                # harvest
                if can_harvest():
                    harvest()

                if get_entity_type() == Entities.Dead_Pumpkin:
                    harvest()

                # plant
                if get_entity_type() == None or get_entity_type() == Entities.Grass:
                    if x <= 1:
                        if y % 2 != x % 2:
                            plant(Entities.Tree)
                    elif 2 <= x <= 3:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        plant(Entities.Carrot)
                    elif 4 <= x <= 5:
                        if get_ground_type() != Grounds.Soil:
                            till()
                        plant(Entities.Pumpkin)

                move(North)
            move(East)