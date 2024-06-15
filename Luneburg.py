import modules.stl_generator_pymesh as stl_gen
import numpy as np
import modules.unit_cells as unit_cells
import modules.geometry as geometry

if __name__ == "__main__":
    filename="test"

    k=10 ## Scale factor (in mm)
    # Generate the sphere mesh
    models=[]
    cube_side_length=0.6
    support_length=0.2
    sphere_radius=5
    size=sphere_radius*2

    models = []

    for z in np.arange(-size/2, size/2, cube_side_length):
        for y in np.arange(-size/2, size/2, cube_side_length):
            for x in np.arange(-size/2, size/2, cube_side_length):
                if geometry.check_point_in_sphere(point=[x, y, z], radius=sphere_radius):
                    cube_side_length_adjusted = cube_side_length * (1 - (((x**2 + y**2+z**2)) * 0.01))
                    model = unit_cells.generate_cubic_unit_cell(
                        cubic_center=[x , y , z ],
                        support_length=support_length,
                        cube_side_lenght=cube_side_length_adjusted,
                        support_side_length=cube_side_length
                    )
                    models.append(model)


    # Fuse the models
    model = stl_gen.merge_models(models=models)

    model_scaled=stl_gen.scale_model(mesh=model,scale_factor=k)

    stl_gen.export_to_stl(mesh=model_scaled,filename=f"{filename}.stl")

    ## Cut model in half to get better cross view
    half_model=stl_gen.merge_models(models=models[0:round(len(models)/3)])
    model_scaled=stl_gen.scale_model(mesh=half_model,scale_factor=k) 
    stl_gen.export_to_stl(mesh=model_scaled,filename=f"{filename}_cross.stl")

    ## Get STL model of unit cells from center and periphery
    stl_gen.export_to_stl(mesh=models[round(len(models)/3)],filename=f"{filename}_unit_cell_center.stl")
    stl_gen.export_to_stl(mesh=models[0],filename=f"{filename}_unit_cell_periphery.stl")
