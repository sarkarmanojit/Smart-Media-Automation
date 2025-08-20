# Photo Sorter

This module contains Python scripts to organize photos using EXIF metadata and AI-based emotion detection.

## Features
- Sort photos by date, location, or camera model using EXIF data
- Detect faces and group photos by emotion (happy, neutral, etc.)
- Rename files and move them into structured folders

## Requirements
- Python 3.9+
- `Pillow`, `exifread`, `opencv-python`, `deepface` (for emotion detection)

## Usage
Run `exif_sort.py` to organize photos by date/location.  
Run `face_emotion_sort.py` to group photos by detected emotion.

```bash
python exif_sort.py
