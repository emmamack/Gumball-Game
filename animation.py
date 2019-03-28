def gumball_animation(time, t_start, layers):
    t_since = time - t_start
    gumball = layers[get_index(layers, Gumball)]

    if  0 < t_since < 150:
        gumball.x += 5
        gumball.y += 5

    return layers
