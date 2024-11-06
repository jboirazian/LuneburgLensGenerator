# Luneburg Lens Genarator


Python script for generating a Luneburg Lens programatically without the use of 3D modeling software based on the [Pymesh](https://github.com/PyMesh/PyMesh) platform

This program was developed for the subject "Medidas electronicas 2" for the UTN FRBA university in the year 2023.

For more information check our [white paper](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/white-paper.pdf)

> [!NOTE]  
> This project is a precursor to [LuneForge](https://github.com/jboirazian/LuneForge)


## How to run it:

You will need [Docker](https://www.docker.com/) for this project.

clone the project , then :

    docker build -t luneburg-gen .

Then:

    docker run -v "$(pwd)":/app -w /app luneburg-gen


# Example of use:

We designed and builded a Luneburg Lens that operated in Band X (8-12 Ghz). We also wanted to use a commercial FDM 3D printer and PLA filament.

Our design parameters were the following:

    k=100 ## Scale factor
    radius = 1.0 ## Unscaled sphere radious
    square_hole_size = 0.2 ## Square hole size lenght
    resolution = 4 ## sphere resolution (4 is fine , for highier resolution increase it , keeping in mind that it will increase the .stl model size)
    step = diameter/16 ## square holes resolution
    hole_variability=(((abs(x*x)+abs(y*y)))+square_hole_size*3)/3

If you want to print this lens , keep in mind to use 100% infill when printing the lens.

You can find this lens on the [Releases section](https://github.com/jboirazian/LuneburgLensGenerator/releases/tag/v1)

## Our results:

Before printing we runned some simulations in CST Studio and confirmed that there was a substantial increase in gain and directivity with our Lens

![cst1](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/imgs/cst1.jpeg)

![cst2](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/imgs/cst2.jpeg)


We were able to run multiple tests in our setup with VNA and 2 horn antennas (one as a transmitter and one as a reciver) and we successfully confimed our Simulations in CST Studio. We dramatically saw a gain in the S12 and S21 parameters of 6 db and more directivity in the beam

![lens1](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/imgs/lens-1.jpeg)
![lens2](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/imgs/lens-2.jpeg)
![lens3](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/imgs/lens-3.jpeg)
![lens4](https://github.com/jboirazian/LuneburgLensGenerator/blob/main/imgs/lens-4.jpeg)





# Contact information:

+ [Juan Agustín Boirazian](https://www.linkedin.com/in/juan-boirazian/)

+ [Juan Ignacio Falabella](https://www.linkedin.com/in/juan-ignacio-falabella-8ba659161/)
