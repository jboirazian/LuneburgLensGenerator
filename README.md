# Luneburg Lens Genarator


### Generated model:

![lunv1-1](https://github.com/jboirazian/LuneburgLensGenerator/assets/21143405/16601dfd-99a9-4fe4-98d7-f734cece412a)
![lunv1-2](https://github.com/jboirazian/LuneburgLensGenerator/assets/21143405/ec67ed3b-37c9-4e6f-af36-0a829b400c8c)
![lunv1-3](https://github.com/jboirazian/LuneburgLensGenerator/assets/21143405/f93634b0-5313-43e4-8cb5-a31ae6ba9cfc)




Python script for generating a Luneburg Lens programatically without the use of 3D modeling software based on the [Pymesh](https://github.com/PyMesh/PyMesh) platform

This program was developed for the subject "Medidas electronicas 2" for the UTN FRBA university in the year 2023.


## How to run it:

You will need [Docker](https://www.docker.com/) for this project.

clone the project , then :

    docker build -t pymesh-test .

Then:

    docker run -v "$(pwd)":/app -w /app pymesh-test


# Example of use:

We designed and builded a Luneburg Lens that operated in Band X (8-12 Ghz). We also wanted to use a commercial FMD 3D printer and PLA filament.

Our design parameters were the following:

    k=100 ## Scale factor
    radius = 1.0 ## Unscaled sphere radious
    square_hole_size = 0.2 ## Square hole size lenght
    resolution = 4 ## sphere resolution (4 is fine , for highier resolution increase it , keeping in mind that it will increase the .stl model size)
    step = diameter/16 ## square holes resolution
    hole_variability=(((abs(x*x)+abs(y*y)))+square_hole_size*3)/3

If you want to print this lens , keep in mind to use 100% infill when printing the lens.




# Contact information:

+ [Juan Agustín Boirazian](https://www.linkedin.com/in/juan-boirazian/)

+ [Juan Ignacio Falabella](https://www.linkedin.com/in/juan-ignacio-falabella-8ba659161/)