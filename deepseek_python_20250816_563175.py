import os
from PIL import Image
from pathlib import Path

def convert_webp_to_jpeg(directory):
    """
    Recursively converts all .webp files in the directory tree to .jpeg format.
    The converted files are saved in the same location as the originals.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.webp'):
                webp_path = os.path.join(root, file)
                jpeg_path = os.path.splitext(webp_path)[0] + '.jpeg'
                
                try:
                    # Open the .webp file and convert to RGB (JPEG doesn't support alpha)
                    with Image.open(webp_path) as img:
                        if img.mode in ('RGBA', 'LA', 'P'):
                            img = img.convert('RGB')
                        img.save(jpeg_path, 'JPEG', quality=95)  # Adjust quality as needed
                    
                    print(f"Converted: {webp_path} -> {jpeg_path}")
                except Exception as e:
                    print(f"Failed to convert {webp_path}: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python convert_webp_to_jpeg.py <directory>")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    if not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory.")
        sys.exit(1)
    
    convert_webp_to_jpeg(target_directory)
    print("Conversion complete!")