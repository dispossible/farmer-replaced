def do_watering():
    if num_items(Items.Water) <= num_drones():
        return

    water_level = get_water()
    if water_level <= num_unlocked(Unlocks.Watering) / 9:
        use_item(Items.Water)

    elif water_level < 1 and num_items(Items.Water) > 100:
        use_item(Items.Water)