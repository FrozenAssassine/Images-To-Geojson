import os
import json
import exifread

def get_gps_coords_and_date(image_path):
    with open(image_path, 'rb') as img_file:
        data = exifread.process_file(img_file, details=False)
        
        if 'GPS GPSLatitude' in data and 'GPS GPSLongitude' in data:
            lat = data['GPS GPSLatitude'].values
            lon = data['GPS GPSLongitude'].values
            lat_ref = data['GPS GPSLatitudeRef'].values
            lon_ref = data['GPS GPSLongitudeRef'].values
            
            lat = convert_to_degrees(lat)
            lon = convert_to_degrees(lon)
            
            if lat_ref != 'N':
                lat = -lat
            if lon_ref != 'E':
                lon = -lon
            
            date_taken = data.get('EXIF DateTimeOriginal')
            date_str = str(date_taken) if date_taken else "Unknown"
            
            return (lat, lon, date_str)
    return None

def convert_to_degrees(value):
    d = float(value[0].num) / float(value[0].den)
    m = float(value[1].num) / float(value[1].den)
    s = float(value[2].num) / float(value[2].den)
    return d + (m / 60.0) + (s / 3600.0)

def make_geojson(points, output_file):
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for point in points:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [point[1], point[0]]
            },
            "properties": {
                "timestamp": point[2]
            }
        }
        geojson_data["features"].append(feature)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(geojson_data, f, indent=4)

    print(f"GeoJSON file saved as {output_file}")

def get_images_with_sub_dirs(folder):
    images = []
    for root, _, files in os.walk(folder):
        images.extend(os.path.join(root, file) for file in files if file.lower().endswith(('jpg', 'jpeg', 'png')))
    return images

def make_and_save_geojson(folder):
    images = get_images_with_sub_dirs(folder)
    gps_points = [get_gps_coords_and_date(img) for img in images]
    gps_points = [point for point in gps_points if point is not None]

    if gps_points:
        make_geojson(gps_points, input("Output Folder: "))
    else:
        print("No GPS data found in any image")

if __name__ == "__main__":
    folder_path = input("Image Folder: ")
    make_and_save_geojson(folder_path)
