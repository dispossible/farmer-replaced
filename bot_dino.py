import util_upgrade
import util_move
import util_math

def bot():
    clear()
    change_hat(Hats.Dinosaur_Hat)

    tail_size = [0]
    target_x, target_y = measure()
    target = {
        'x': target_x,
        'y': target_y
    }

    last_pos = {
        'x': get_pos_x(),
        'y': get_pos_y(),
        'strikes': 0
    }

    def update_target():
        target_x, target_y = measure()
        target['x'] = target_x
        target['y'] = target_y

    def reset():
        change_hat(Hats.Straw_Hat)
        change_hat(Hats.Dinosaur_Hat)
        tail_size[0] = 0
        update_target()
    
    def on_move(x, y):
        if get_entity_type() == Entities.Apple:
            tail_size[0] += 1
            update_target()
        # If stuck, reset the map
        if last_pos["x"] == get_pos_x() and last_pos["y"] == get_pos_y():
            if last_pos["strikes"] >= 3:
                reset()
            else:
                last_pos["strikes"] += 1
        else:
            last_pos["strikes"] = 0
        last_pos["x"] = get_pos_x()
        last_pos["y"] = get_pos_y()

    # Get the first apple
    util_move.move_to_nowrap(target['x'], target['y'], on_move)
    
    while True:
        util_upgrade.buy_upgrades()
        
        # Check if can afford to play
        play_cost = get_cost(Entities.Apple)
        can_afford = True
        for item in play_cost:
            if num_items(item) < play_cost[item]:
                can_afford = False
        if not can_afford:
            return

        world_size = get_world_size()

        verticals_filled = (tail_size[0] + 1) / (world_size - 1)

        # While small, go up and down
        if verticals_filled < 1.9:
            if get_pos_y() != world_size - 1:
                util_move.move_to_nowrap(get_pos_x(), world_size - 1, on_move)
            util_move.move_to_nowrap(target['x'], target['y'], on_move)
            util_move.move_to_nowrap(get_pos_x(), 0, on_move)
            util_move.move_to_nowrap(target['x'], target['y'], on_move)

        # Now large, do zig zags
        elif verticals_filled < world_size * 0.55:
            # If out of position, move back to the start
            if get_pos_x() != 0 or get_pos_y() != 1:
                util_move.move_to_nowrap(get_pos_x(), world_size - 1, on_move)
                util_move.move_to_nowrap(world_size - 1, 0, on_move)
                util_move.move_to_nowrap(0, 1, on_move)

            # Zig zag until the entire tail is on the left
            util_move.move_zig_zag(util_math.ceil(verticals_filled), world_size - 1, East, North, on_move)

            # The apple is out of play, move to the right edge and catch it on the return
            if target['y'] == 0:
                util_move.move_to_nowrap(world_size - 1, get_pos_y(), on_move)
            # It's on the right edge, need to make sure we don't block ourselves
            elif target['x'] == world_size - 1:
                util_move.move_to_nowrap(target['x'] - 1, target['y'], on_move)
                util_move.move_to_nowrap(target['x'], target['y'], on_move)
            else:
                # Move to the apple
                while target['x'] > get_pos_x() and target['y'] > 0 and target["x"] < world_size - 1:
                    util_move.move_to_nowrap(target['x'], target['y'], on_move)

            # Move back to the left
            util_move.move_to_nowrap(world_size - 1, 0, on_move)
            util_move.move_to_nowrap(0, 0, on_move)
            util_move.move_to_nowrap(0, 1, on_move)

        # Fully grown, fill the entire map
        else:
            util_move.move_zig_zag(world_size, world_size - 1, East, North, on_move)

            # Move back to the left
            util_move.move_to_nowrap(world_size - 1, 0, on_move)
            util_move.move_to_nowrap(0, 0, on_move)
            util_move.move_to_nowrap(0, 1, on_move)



    
if __name__ == "__main__":
    bot()