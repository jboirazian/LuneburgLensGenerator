### Best itereations:

    square_hole_size = 0.4
    radius = 1.0
    diameter = radius*2
    smaller_radius = 0.2
    resolution = 500
    step = square_hole_size/2


    hole_variability=((abs(x)+abs(y)+abs(square_hole_size))/2)


### 29 septiembre best iteration:

    square_hole_size = 0.4*scale_factor
    radius = 1.0*scale_factor
    diameter = radius*2
    resolution = 500
    step = square_hole_size/8

    hole_variability=(((abs(x*x)+abs(y*y)))+square_hole_size)/2
    square_holes.append({'size': square_hole_size*hole_variability, 'position': np.array([x, y, radius])})



    square_hole_size = 0.6
    radius = 1.0
    diameter = radius*2
    resolution = 500
    step = square_hole_size/6
    hole_variability=(((abs(x*x)+abs(y*y)))+square_hole_size*2)/2

