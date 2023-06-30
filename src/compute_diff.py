import numpy as np
import trimesh
import sys

def scale_mesh(mesh, scale):
    # Compute the current dimensions of the bounding box
    min_bounds, max_bounds = mesh.bounds
    current_dimensions = max_bounds - min_bounds

    # Compute the transformation matrix to scale the mesh
    scale_factors = scale / current_dimensions
    transformation_matrix = np.diag(np.append(scale_factors, 1))

    # Apply the transformation
    mesh.apply_transform(transformation_matrix)

def compute_distance(ref_path, rec_path):
    # Load the reference and reconstructed meshes
    ref_mesh = trimesh.load_mesh(ref_path, process=False)
    rec_mesh = trimesh.load_mesh(rec_path, process=False)

    # Ensure the meshes are triangulated
    ref_mesh = ref_mesh.split(only_watertight=False)[0]
    rec_mesh = rec_mesh.split(only_watertight=False)[0]

    # Scale the meshes to the same size
    ref_min_bounds, ref_max_bounds = ref_mesh.bounds
    ref_scale = ref_max_bounds - ref_min_bounds
    scale_mesh(rec_mesh, ref_scale)

    # Compute the nearest point on the reference mesh for each vertex of the reconstructed mesh
    closest_points, distance, triangle_id = ref_mesh.nearest.on_surface(rec_mesh.vertices)

    # Compute the mean distance
    mean_distance = np.mean(distance)

    return mean_distance

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <reference_obj_path> <reconstructed_obj_path>")
        sys.exit(1)

    ref_path = sys.argv[1]
    rec_path = sys.argv[2]

    mean_distance = compute_distance(ref_path, rec_path)
    print(f'The mean distance between the reference and reconstructed model is: {mean_distance}')

if __name__ == "__main__":
    main()
