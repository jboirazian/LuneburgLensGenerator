import modules.stl_generator_pymesh as stl_gen
import numpy as np
import modules.unit_cells as unit_cells

if __name__ == "__main__":


    k=100 ## Scale factor (in mm)
    radius = 1.0 ## Unscaled sphere radious (in mm)
    square_hole_size = 0.2 ## Square hole size lenght (in mm)
    diameter = radius*2
    resolution = 4 ## sphere resolution (4 is fine , for highier resolution increase it , keeping in mind that it will increase the .stl model size)
    step = diameter/16 ## square holes resolution (in mm)

    print("Started process...")
    # Generate the sphere mesh
    model= unit_cells.generate_sphere_unit_cell()

    model_scaled=stl_gen.scale_model(mesh=model,scale_factor=k)

    print("Exporting model to .stl")
    stl_gen.export_to_stl(mesh=model_scaled,filename="test.stl")
    
    print("Done!")
