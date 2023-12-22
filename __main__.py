from datetime import datetime
from os import mkdir, rmdir
import os
import numpy as np
from convert_map_type import convert_embedded_gltf_to_separated_gltf, convert_map_to_embedded_gltf, convert_map_to_obj
from download_map_osm import download_file_with_bbox
from rotate_map import rotate_gltf_file, rotate_obj_file
import shutil

bbox_coordinates = [22.06813,50.60732,22.08498,50.61350] # left, buttom, right, top

rotation_matrix = np.array([[1,  0,  0],
                            [0, -1,  0],
                            [0,  0, -1]])
rotation_quaterion = [1, 0, 0, 0]

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
    convert_embedded_gltf_to_separated_gltf("temp/model.gltf", out_directory + "/model/model.gltf")

    shutil.rmtree("temp", ignore_errors=True)

if __name__ == "__main__":
    generate_map()