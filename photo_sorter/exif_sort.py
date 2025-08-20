# This script will sort photos based on EXIF metadata
```python
import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_exif_date(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == 'DateTimeOriginal':
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
    return None

def sort_photos_by_date(folder):
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            full_path = os.path.join(folder, filename)
            date = get_exif_date(full_path)
            if date:
                target_folder = os.path.join(folder, date.strftime('%Y-%m-%d'))
                os.makedirs(target_folder, exist_ok=True)
                os.rename(full_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {target_folder}")
            else:
                print(f"No EXIF date found for {filename}")

if __name__ == "__main__":
    sort_photos_by_date("your_photo_folder_here")
