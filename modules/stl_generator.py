import numpy as np
from stl import stl,mesh

def generate_sphere(radius, resolution):
    phi = np.linspace(0, np.pi, resolution)
    theta = np.linspace(0, 2 * np.pi, resolution)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    vertices = np.array([x.flatten(), y.flatten(), z.flatten()]).T

    return vertices




def add_square_holes(vertices, holes):
    """
    Add square holes to the Lunenburg lens.

    Parameters:
    - vertices: 3D coordinates of lens vertices.
    - holes: List of dictionaries, each specifying a hole with keys 'size' and 'position'.

    Returns:
    - Updated vertices after adding the square holes.
    """
    for hole in holes:
        hole_size = hole['size']
        hole_position = hole['position']

        # Compute distance to square hole center
        distance_to_hole = (np.max(np.abs(vertices[:, :2] - hole_position[:2]), axis=1))*4
        hole_mask = distance_to_hole*2 < hole_size / 2

        # Subtract cubic region for the square hole
        vertices[hole_mask, 2] = np.minimum(
            vertices[hole_mask, 2], -hole_size / 2)

    return vertices

def add_square_holes_through_all(vertices, holes, through_value=-1.0):
    """
    Add square holes to the Lunenburg lens, going through the entire object.

    Parameters:
    - vertices: 3D coordinates of lens vertices.
    - holes: List of dictionaries, each specifying a hole with keys 'size' and 'position'.
    - through_value: Value to set for the z-coordinate inside the hole.

    Returns:
    - Updated vertices after adding the square holes.
    """
    for hole in holes:
        hole_size = hole['size']
        hole_position = hole['position']

        # Compute distance to square hole center
        distance_to_hole = np.max(np.abs(vertices[:, :2] - hole_position[:2]), axis=1)
        hole_mask = distance_to_hole < hole_size / 2

        # Set z-coordinate to through_value for the vertices within the hole
        vertices_inside_hole = vertices[hole_mask]
        vertices_inside_hole[:, 2] = through_value
        vertices[hole_mask] = vertices_inside_hole

    return vertices


def save_stl(vertices, filename='sphere_with_through_holes.stl'):
    faces = []
    resolution = int(np.sqrt(vertices.shape[0]))

    for i in range(resolution - 1):
        for j in range(resolution - 1):
            p0 = i * resolution + j
            p1 = (i + 1) * resolution + j
            p2 = (i + 1) * resolution + (j + 1)
            p3 = i * resolution + (j + 1)
            faces.extend([[p0, p1, p2], [p0, p2, p3]])

    faces = np.array(faces)

    # Create the mesh
    mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, face in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = vertices[face[j], :]

    # Save the mesh as an STL file
    mesh_data.save(filename, mode=stl.Mode.BINARY)


def cut_sphere_in_half(vertices, cut_plane_height):
    """
    Cut a sphere in half along a specified plane.

    Parameters:
    - vertices: 3D coordinates of the sphere vertices.
    - cut_plane_height: Height at which to cut the sphere.

    Returns:
    - Updated vertices after cutting the sphere.
    """
    cut_mask = vertices[:, 2] < cut_plane_height
    vertices[cut_mask, 2] = cut_plane_height
    return vertices