# 📍 Images to GeoJSON

A simple Python script that extracts **GPS coordinates** and **timestamps** from images and saves them as a **GeoJSON file** for easy visualization and mapping.

## 🚀 Features
- Extracts **GPS latitude, longitude, and timestamp** from images
- Saves the data in **GeoJSON format**
- Scans the root folder recursively for images
- Works with JPG, JPEG and PNG images

## 🛠 Installation
```bash
# Clone the repository
git clone https://github.com/FrozenAssassine/Images-To-Geojson.git
cd Images-To-Geojson

# Install dependencies
pip install exifread
```

## 📷 Usage
```bash
# Run the script
python images_to_geojson.py
```
1. Enter the root folder path containing images when prompted (scans recursively)
2. Enter output path or file when prompted

## 📄 Output Example
```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": { "type": "Point", "coordinates": [8.6821, 50.1109] },
            "properties": { "timestamp": "2024:03:27 15:34:12" }
        }
    ]
}
```
