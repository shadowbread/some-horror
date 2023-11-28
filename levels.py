import level

levels_list = [level.Level(600, 600)]
levels_list[0].add_wall(100, 0, 5, 100)
levels_list[0].add_wall(0, 150, 150, 5)
levels_list[0].add_wall(150, 100, 5, 150)
levels_list[0].add_wall(70, 250, 150, 5)
levels_list[0].add_wall(215, 150, 5, 100)
levels_list[0].add_wall(215, 200, 150, 5)


levels_list[0].add_thorn(100, 100, 50)
levels_list[0].add_angry_square(300, 300, "x", 200, 400, 5)

    # {'x': 300, 'y': 200, 'width': 5, 'height':300},
    # {'x': 0, 'y': 500, 'width': 200, 'height':5},
    # {'x': 100, 'y': 450, 'width': 200, 'height':5},
    # {'x': 0, 'y': 400, 'width': 200, 'height':5},
    # {'x': 100, 'y': 350, 'width': 200, 'height':5},
    # {'x': 250, 'y': 50, 'width': 400, 'height':5},
    # {'x': 500, 'y': 50, 'width': 5, 'height':100},
    # {'x': 450, 'y': 450, 'width': 250, 'height':5},
    # {'x': 450, 'y': 250, 'width': 5, 'height':200},
