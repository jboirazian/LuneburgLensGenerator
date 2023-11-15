import modules.stl_generator_pymesh as stl_gen
import numpy as np

if __name__ == "__main__":


    k=100 ## Scale factor (in mm)
    radius = 1.0 ## Unscaled sphere radious (in mm)
    square_hole_size = 0.2 ## Square hole size lenght (in mm)
    diameter = radius*2
    resolution = 4 ## sphere resolution (4 is fine , for highier resolution increase it , keeping in mind that it will increase the .stl model size)
    step = diameter/16 ## square holes resolution (in mm)

    print("Started process...")
    # Generate the sphere mesh
    sphere = stl_gen.generate_sphere(radius=radius,resolution=resolution)

    print("Sphere generated. Adding holes...")

    for y in np.arange(-diameter, diameter, step):
        for x in np.arange(-diameter, diameter, step):
            hole_variability=(((abs(x*x)+abs(y*y)))+square_hole_size*3)/3
            A=square_hole_size*hole_variability
            sphere=stl_gen.add_square_hole_to_mesh(L=diameter,A=A,xy_position=[x,y],mesh=sphere)

    print("Luneburg lens generated , scaling up...")
    # Scale up the mesh
    scaled_sphere=stl_gen.scale_model(mesh=sphere,scale_factor=k)

    print("Exporting model to .stl")
    stl_gen.export_to_stl(mesh=scaled_sphere,filename="luneburg.stl")
    
    print("Done!")
