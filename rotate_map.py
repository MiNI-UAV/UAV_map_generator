from pygltflib import GLTF2
import numpy as np

def rotate_gltf_file(input_file, output_file, rotation_quaterion):
    # Load the glTF file
    map = GLTF2().load(input_file)
    map.nodes[0].rotation = rotation_quaterion
    map.save(output_file)

def rotate_obj_file(input_file, output_file, rotation_matrix):
    # Read the input OBJ file
    with open(input_file, 'r') as input_obj:
        lines = input_obj.readlines()

    rotated_lines = []
    for line in lines:
        if line.startswith('v '):  # Process vertex lines
            # Extract vertex coordinates
            vertex_coords = list(map(float, line.strip().split()[1:]))
            vertex_coords_np = np.array([vertex_coords])

            # Rotate the vertex coordinates using the quaternion
            rotated_vertex_coords = vertex_coords_np.dot(rotation_matrix)

            # Update the line with the rotated vertex coordinates
            rotated_line = f'v {rotated_vertex_coords[0][0]} {rotated_vertex_coords[0][1]} {rotated_vertex_coords[0][2]}\n'
            rotated_lines.append(rotated_line)
        else:
            # just copy
            rotated_lines.append(line)

    with open(output_file, 'w') as output_obj:
        output_obj.writelines(rotated_lines)
    

if __name__ == "__main__":
    # Example usage
    input_file = "model.gltf"
    output_file = "model_rotated.gltf"
    rotation = [1, 0, 0, 0] #  (x,y,z,w)
    rotate_gltf_file(input_file, output_file, rotation)

    input_file = "map.obj"
    output_file = "map_rotated.obj"
    rotation_matrix = np.array([[-1,  0,  0],
                                [ 0, -1,  0],
                                [ 0,  0, -1]])
    rotate_obj_file(input_file, output_file, rotation_matrix)
    

