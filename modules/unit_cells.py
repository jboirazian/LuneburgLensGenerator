import modules.stl_generator_pymesh as stl_gen



def generate_cubic_unit_cell():
    ### Unit cell based of the "A Highly Efficient Energy Harvesting Circuit Using Luneburg Lens"
    ### you will find it in docs folder

    ### Make the initial center cube
    cube= stl_gen.generate_prism(L=1,A=1,xy_positon=[0,0])
    models=[cube]
    ### Then make all the 6 joints
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[0.5,0]))
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[-0.5,0]))
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[0,0.5]))
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[0,-0.5]))

    return stl_gen.fuse_models(models=models)



def generate_sphere_unit_cell():
    ### Unit cell based of the "A Highly Efficient Energy Harvesting Circuit Using Luneburg Lens"
    ### you will find it in docs folder

    ### Make the initial center sphere
    sphere= stl_gen.generate_sphere(radius=1,resolution=4)
    models=[sphere]
    ### Then make all the 6 joints
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[1,0]))
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[-1,0]))
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[0,1]))
    models.append(stl_gen.generate_prism(L=0.1,A=0.1,xy_positon=[0,-1]))

    return stl_gen.fuse_models(models=models)