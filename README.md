### Generated model:

![lunv1-1](https://github.com/jboirazian/LuneburgLensGenerator/assets/21143405/16601dfd-99a9-4fe4-98d7-f734cece412a)
![lunv1-2](https://github.com/jboirazian/LuneburgLensGenerator/assets/21143405/ec67ed3b-37c9-4e6f-af36-0a829b400c8c)
![lunv1-3](https://github.com/jboirazian/LuneburgLensGenerator/assets/21143405/f93634b0-5313-43e4-8cb5-a31ae6ba9cfc)


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

