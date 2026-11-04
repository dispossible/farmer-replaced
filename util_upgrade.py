import util_list

def buy_upgrades(leeway = 50):
    for upgrade in Unlocks:
        costs = get_cost(upgrade)

        if costs:
            can_afford = True

            for item in costs:
                owned = num_items(item)
                if owned - leeway < costs[item]:
                    can_afford = False
            
            if can_afford:
                unlock(upgrade)


def get_crop_requirements():
    all_costs = {}
    for upgrade in Unlocks:
        costs = get_cost(upgrade)
        if costs:
            for item in costs:
                if num_unlocked(item) > 0:
                    if item not in all_costs:
                        all_costs[item] = 0
                    all_costs[item] += costs[item]
    crops = []
    for crop in all_costs:
        if crop == Items.Hay:
            crops.append(Entities.Grass)
        elif crop == Items.Wood:
            if num_unlocked(Entities.Tree) == 0:
                crops.append(Entities.Bush)
            else:
                crops.append(Entities.Tree)
        elif crop == Items.Carrot:
            crops.append(Entities.Carrot)
        elif crop == Items.Pumpkin:
            crops.append(Entities.Pumpkin)
        elif crop == Items.Cactus:
            crops.append(Entities.Cactus)
        else:
            crops.append(crop)
    return crops