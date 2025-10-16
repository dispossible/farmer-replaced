def buy_upgrades():
    for upgrade in Unlocks:
        costs = get_cost(upgrade)

        if costs:
            can_afford = True

            for item in costs:
                owned = num_items(item)
                if owned - 50 < costs[item]:
                    can_afford = False
            
            if can_afford:
                unlock(upgrade)
                do_a_flip()
                pet_the_piggy()
