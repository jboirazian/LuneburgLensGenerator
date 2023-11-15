# Luneburg Lens Genarator


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


## Our results:

Before printing 


We were able to run multiple tests in our setup with VNA and 2 horn antennas (one as a transmitter and one as a reciver) and we successfully confimed our Simulations in CST Studio. We dramatically saw a gain in the S12 and S21 parameters of 6 db and more directivity in the beam







# Contact information:

+ [Juan Agustín Boirazian](https://www.linkedin.com/in/juan-boirazian/)

+ [Juan Ignacio Falabella](https://www.linkedin.com/in/juan-ignacio-falabella-8ba659161/)