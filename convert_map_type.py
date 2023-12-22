import subprocess

osm2world_path = "OSM2World/target/osm2world-0.4.0-SNAPSHOT.jar"
config_file = "config.properties"

def run_osm2world_command(input_file, output_file):
    try:
        command = f"java -jar {osm2world_path} --input {input_file} --output {output_file} --config {config_file}"
        subprocess.run(command, check=True, shell=True)
        print(f"OSM2World generated {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def convert_map_to_obj(input_file, output_file = "map.obj"):
    run_osm2world_command(input_file, output_file)

def convert_map_to_embedded_gltf(input_file, output_file = "map.gltf"):
    run_osm2world_command(input_file,output_file)

def convert_embedded_gltf_to_separated_gltf(input_file, output_file):
    try:
        command = f"gltf-pipeline  --input {input_file} --output {output_file} --separate"
        subprocess.run(command, check=True, shell=True)
        print(f"gltf-pipeline generated {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = "map.osm"
    convert_map_to_embedded_gltf(input_file)
    convert_map_to_obj(input_file)
    convert_embedded_gltf_to_separated_gltf("map.gltf", "model.gltf")
    