def do_fertilize():
    cures = num_items(Items.Weird_Substance)

    if cures < 1:
        return