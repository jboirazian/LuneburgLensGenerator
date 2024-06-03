import modules.stl_generator_pymesh as stl_gen
import numpy as np
import modules.unit_cells as unit_cells
import modules.geometry as geometry

if __name__ == "__main__":
    k=10 ## Scale factor (in mm)
    print("Started process...")
    # Generate the sphere mesh
    models=[]
    size=10
    cube_side_length=0.4
    support_length=0.2
    sphere_radius=5

    models = [
        unit_cells.generate_cubic_unit_cell(
            cubic_center=[x + support_length * x, y + support_length * y, z + support_length * z],
            support_length=support_length,
            cube_side_length=cube_side_length
        )
        for z in np.arange(-size/2, size/2, cube_side_length)
        for y in np.arange(-size/2, size/2, cube_side_length)
        for x in np.arange(-size/2, size/2, cube_side_length)
        if geometry.check_point_in_sphere(point=[x, y, z], radius=sphere_radius)
    ]


    # Fuse the models
    print(f"Fusing {len(models)} unit cells")
    model = stl_gen.merge_models(models=models)
    print("Done!")

    model_scaled=stl_gen.scale_model(mesh=model,scale_factor=k)

    print("Exporting model to .stl")
    stl_gen.export_to_stl(mesh=model_scaled,filename="test.stl")
    stl_gen.export_to_stl(mesh=models[0],filename="unit_cell.stl")
    
    print("Done!")
