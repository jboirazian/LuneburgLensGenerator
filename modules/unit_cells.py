import modules.stl_generator_pymesh as stl_gen



def generate_cubic_unit_cell(cubic_center:list=[0,0,0],support_length:int=0,cube_side_length:int=0):
    ### Unit cell based of the "A Highly Efficient Energy Harvesting Circuit Using Luneburg Lens"
    ### you will find it in docs folder

    ### Make the initial center cube
    cube=stl_gen.generate_prism(L=cube_side_length,A=cube_side_length,xyz_position=cubic_center)
    models=[cube]
    ### Then make all the 6 joints
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[cubic_center[0]+cube_side_length/2,cubic_center[1],cubic_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[cubic_center[0]-cube_side_length/2,cubic_center[1],cubic_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[cubic_center[0],cubic_center[1]+cube_side_length/2,cubic_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[cubic_center[0],cubic_center[1]-cube_side_length/2,cubic_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[cubic_center[0],cubic_center[1],cubic_center[2]+cube_side_length/2]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[cubic_center[0],cubic_center[1],cubic_center[2]-cube_side_length/2]))
    
    print(f"Generating cell at {cubic_center}")
    unit_cell=stl_gen.merge_models(models=models)
    print(f"Done!")
    return unit_cell



def generate_sphere_unit_cell(sphere_center:list=[0,0,0],support_length:int=0,sphere_radius:int=0):
    ### Unit cell based of the "A Highly Efficient Energy Harvesting Circuit Using Luneburg Lens"
    ### you will find it in docs folder

    ### Make the initial center sphere
    sphere= stl_gen.generate_sphere(radius=sphere_radius,resolution=2,center=sphere_center)
    models=[sphere]
    ### Then make all the 6 joints
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[sphere_center[0]+sphere_radius,sphere_center[1],sphere_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[sphere_center[0]-sphere_radius,sphere_center[1],sphere_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[sphere_center[0],sphere_center[1]+sphere_radius,sphere_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[sphere_center[0],sphere_center[1]-sphere_radius,sphere_center[2]]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[sphere_center[0],sphere_center[1],sphere_center[2]+sphere_radius]))
    models.append(stl_gen.generate_prism(L=support_length,A=support_length,xyz_position=[sphere_center[0],sphere_center[1],sphere_center[2]-sphere_radius]))

    print(f"Generating cell at {sphere_center}")
    unit_cell=stl_gen.merge_models(models=models)
    print(f"Done!")
    return unit_cell