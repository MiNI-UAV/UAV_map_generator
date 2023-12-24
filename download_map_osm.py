import requests

# Download *.osm map file from OSM API.
def download_file_with_bbox(bbox : list[float], destination : str):
    assert(len(bbox) == 4)
    try:
        url = f"https://overpass-api.de/api/map?bbox={','.join(map(str, bbox))}"
        response = requests.get(url)
        
        with open(destination, 'wb') as file:
            file.write(response.content)
        
        print(f"File downloaded successfully to {destination}")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    # Example usage
    bbox_coordinates = [22.0601,50.5953,22.1224,50.6212]
    destination_file = "map.osm"
    download_file_with_bbox(bbox_coordinates, destination_file)