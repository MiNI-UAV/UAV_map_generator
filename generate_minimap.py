import cairosvg
from math import radians, sin, cos, sqrt, atan2
import subprocess

import numpy as np

def get_boundary_from_obj(input_file):
    # Read the input OBJ file
    with open(input_file, 'r') as input_obj:
        lines = input_obj.readlines()

    futher_point = [0.0, 0.0]
    for line in lines:
        if line.startswith('v '):  # Process vertex lines
            # Extract vertex coordinates
            vertex_coords = list(map(float, line.strip().split()[1:3]))
            res = [abs(elem) for elem in vertex_coords]
            futher_point = [max(left,right) for (left, right) in zip(futher_point, res)]
    return [2.*elem for elem in futher_point]

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    radius = 6371000
    distance = radius * c
    return distance

def bbox_to_rectangle(bbox_coordinates):
    left, bottom, right, top = bbox_coordinates

    # Calculate the center of the bounding box
    center_lat = (bottom + top) / 2
    center_lon = (left + right) / 2

    # Calculate the width and height of the bounding box
    width = haversine(center_lat, left, center_lat, right)
    height = haversine(bottom, center_lon, top, center_lon)

    return width, height

def generate_svg_map(osm_file, output_file):
    try:
        command = f"map-machine render -i {osm_file} -o {output_file}"
        subprocess.run(command, check=True, shell=True)
        print(f"Map-machine generated svg map: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def generate_minimap(osm_file, bbox_coordinates, output_file):
    generate_svg_map(osm_file,"temp/minimap.svg")
    rectangle_dimensions = bbox_to_rectangle(bbox_coordinates)
    output_width = int(rectangle_dimensions[0]*2)
    output_height = int(rectangle_dimensions[1]*2)
    cairosvg.svg2png(url="temp/minimap.svg", write_to=output_file,
        output_width=output_width, output_height=output_height)
    
def coordinates_to_xy(center_lat, center_lon, target_lat, target_lon):
    x = haversine(center_lat, center_lon, center_lat, target_lon)*np.sign(target_lon-center_lon)
    y = haversine(center_lat, center_lon, target_lat, center_lon)*np.sign(target_lat-center_lat)
    return [x, y]

