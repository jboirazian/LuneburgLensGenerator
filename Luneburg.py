import modules.stl_generator_pymesh as stl_gen
import numpy as np
import modules.unit_cells as unit_cells

if __name__ == "__main__":
    k=10 ## Scale factor (in mm)
    print("Started process...")
    # Generate the sphere mesh
    models=[]
    size=10
    # Optimize the nested loop with list comprehension
    models = tuple(
        unit_cells.generate_cubic_unit_cell(
            cubic_center=[x + 0.1 * x, y + 0.1 * y, z + 0.1 * z],
            support_length=0.1,
            cube_side_length=1
        )
        for z in range(size)
        for y in range(size)
        for x in range(size)
    )

    # Fuse the models
    print("Fusing all unit cells")
    model = stl_gen.fuse_models(models=models)


    model_scaled=stl_gen.scale_model(mesh=model,scale_factor=k)

    print("Exporting model to .stl")
    stl_gen.export_to_stl(mesh=model_scaled,filename="test.stl")
    
    print("Done!")
