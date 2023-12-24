from datetime import datetime
from os import mkdir, rmdir
import os
import numpy as np
from assign_materials import assign_materials_colors
from convert_map_type import convert_embedded_gltf_to_separated_gltf, convert_map_to_embedded_gltf, convert_map_to_obj
from download_map_osm import download_file_with_bbox
from generate_minimap import coordinates_to_xy, generate_minimap
from rotate_map import rotate_gltf_file, rotate_obj_file
import shutil

bbox_coordinates = [21.00425,52.21979,21.01293,52.22309] # left, buttom, right, top

target_coordinates = [52.22217,21.007] #some point on map latitiude, longitiude

rotation_matrix = np.array([[ 0,  1,  0],
                            [ 0,  0, -1],
                            [-1,  0,  0]])
rotation_quaterion = [-0.5,-0.5, 0.5, 0.5 ]

def generate_map():
    if not os.path.exists("out"):
        os.makedirs("out")
    if os.path.exists("temp"):
        shutil.rmtree("temp", ignore_errors=True)
    mkdir("temp")
    out_directory = f"out/gen_{round(datetime.timestamp(datetime.now()))}" 
    mkdir(out_directory)
    mkdir(out_directory + "/model")
    mkdir(out_directory + "/textures")

    download_file_with_bbox(bbox_coordinates,"temp/map.osm")
    convert_map_to_obj("temp/map.osm","temp/map.obj")
    rotate_obj_file("temp/map.obj",out_directory + "/model/model.obj", rotation_matrix)
    convert_map_to_embedded_gltf("temp/map.osm","temp/map.gltf")
    rotate_gltf_file("temp/map.gltf","temp/model.gltf", rotation_quaterion)
    assign_materials_colors("temp/model.gltf","temp/model_colored.gltf")
    convert_embedded_gltf_to_separated_gltf("temp/model_colored.gltf", out_directory + "/model/model.gltf")
    generate_minimap("temp/map.osm",bbox_coordinates,out_directory + "/model/minimap.png")
    shutil.rmtree("temp", ignore_errors=True)

if __name__ == "__main__":
    # Generate assets
    generate_map()

    # Calculate target pos on map
    target_xy = coordinates_to_xy((bbox_coordinates[3]+bbox_coordinates[1])/2,
                                  (bbox_coordinates[2]+bbox_coordinates[0])/2,
                                  target_coordinates[0],target_coordinates[1])
    print(f"Target (x,y): {target_xy}")