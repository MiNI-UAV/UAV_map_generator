from pygltflib import GLTF2
import numpy as np

materials_params = {
    #MATERIAL_NAME : (RGBA, metallic, roughness)
    "TERRAIN_DEFAULT"               : ([0.00, 1.00, 0.00, 1.00], 1.00, 1.00),
    "TREE_BILLBOARD_CONIFEROUS"     : ([0.00, 0.50, 0.00, 1.00], 1.00, 1.00),
    "BUILDING_DEFAULT"              : ([1.00, 0.90, 0.55, 1.00], 1.00, 1.00),
    "POWER_TOWER_VERTICAL"          : ([0.75, 0.75, 0.75, 1.00], 1.00, 1.00),
    "ASPHALT"                       : ([0.30, 0.30, 0.30, 1.00], 1.00, 1.00),
    "WATER"                         : ([0.00, 0.50, 1.00, 1.00], 1.00, 1.00),
    "WOOD"                          : ([0.50, 0.25, 0.00, 1.00], 1.00, 1.00),
    "FIREHYDRANT"                   : ([1.00, 0.00, 0.00, 1.00], 1.00, 1.00),
    "STEEL"                         : ([0.80, 0.80, 0.80, 1.00], 1.00, 1.00),
    "GRASS"                         : ([0.00, 0.80, 0.00, 1.00], 1.00, 1.00),
    "TREE_BILLBOARD_BROAD_LEAVED"   : ([0.00, 0.50, 0.00, 1.00], 1.00, 1.00),
    "GRAVEL"                        : ([0.40, 0.40, 0.40, 1.00], 1.00, 1.00),
    "BRIDGE_DEFAULT"                : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
    "EARTH"                         : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
    "SCRUB"                         : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
    "RAIL_BALLAST"                  : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
    "PITCH_SOCCER"                  : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
    "PLASTIC"                       : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
    "GARAGE_DOOR"                   : ([1.0, 1.0, 1.0, 1.0], 1.0, 1.0),
}

def assign_materials_colors(input_file, output_file):
    # Load the glTF file
    map = GLTF2().load(input_file)
    for material in map.materials:
        if material.name in materials_params:
            params = materials_params[material.name]
            material.pbrMetallicRoughness.baseColorFactor = params[0]
            material.pbrMetallicRoughness.metallicFactor  = params[1]
            material.pbrMetallicRoughness.roughnessFactor = params[2]

        else:
            print(f"Unknown material: {material.name}")
    map.save(output_file)


if __name__ == "__main__":
    # Example usage
    input_file = "map.gltf"
    output_file = "colored.gltf"

    assign_materials_colors(input_file, output_file)