# Installation

## 1. Nodejs
Install nodejs: nodejs.org. On Ubuntu or similar you may use Snap:
sudo snap install node --classic

Next install gltf-pipeline
npm install -g gltf-pipeline

## 2. Install libraries
sudo apt-get install geos libgeos-dev libcairo2-dev

## 3. Python
Create environment with Python 3.9.
Install map-machine:
    pip install git+https://github.com/enzet/map-machine
Install other requierments.

## 4. OSM2World
Download and build OSM2World. Java is needed.
Project site: https://osm2world.org/
Set proper path in convert_map_osm.py

# Usage

1. Set boundary box and target coordinates in __main__.py.
2. Run script
