def make_tea():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cups
    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    pour("boiled_water")
    stir("tea")
    serve("tea")
    
make_tea()
