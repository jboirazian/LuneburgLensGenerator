from matplotlib import pyplot as plt
import modules.stl_generator as stl_gen
import numpy as np


if __name__ == "__main__":
    # Set the radius and resolution

    square_hole_size = 0.6
    radius = 1.0
    diameter = radius*2
    resolution = 1000
    step = square_hole_size/6

    hole_variability_list=[]

    # Generate the sphere mesh
    vertices = stl_gen.generate_sphere(radius, resolution)

    # Specify through hole positions and size
    square_holes = []

    for x in np.arange(-diameter, diameter, step):
        for y in np.arange(-diameter, diameter, step):
            hole_variability=(((abs(x*x)+abs(y*y)))+square_hole_size*2)/2
            square_holes.append({'size': square_hole_size*hole_variability, 'position': np.array([x, y, diameter])})
            hole_variability_list.append(square_hole_size*hole_variability)

    plt.plot(hole_variability_list)
    plt.show()

    # Add through holes to the sphere
    vertices = stl_gen.add_square_holes(vertices=vertices,holes=square_holes)

    # # Cut the sphere in half along the z-plane at a specific height
    cut_plane_height = 0.0
    vertices = stl_gen.cut_sphere_in_half(vertices.copy(), cut_plane_height)

    # Save the mesh as an STL file
    stl_gen.save_stl(vertices=vertices, filename="luneburg_v1.stl")
