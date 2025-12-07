#!/usr/bin/env python3
"""
CK3 Terrain Mask Converter - Standalone Console Version
Converts PNG files to 4608x2304 resolution and 8-bit grayscale for CK3 1.18+ terrain masks

Requirements: pip install Pillow

Usage: python ck3_mask_converter.py input_folder output_folder
"""

import os
import sys
import glob
from PIL import Image

def convert_png_files(input_dir, output_dir, target_width=4608, target_height=2304):
    """
    Convert all PNG files in input directory to target resolution and 8-bit grayscale
    
    Parameters:
    input_dir: Directory containing source PNG files
    output_dir: Directory to save converted files (as 8-bit grayscale)
    target_width: Target width (default: 4608 for TC Sandbox scale)
    target_height: Target height (default: 2304 for TC Sandbox scale)
    """
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Find all PNG files
    png_pattern = os.path.join(input_dir, "*.png")
    png_files = glob.glob(png_pattern, recursive=False)
    
    # Also check for uppercase extension
    png_pattern_upper = os.path.join(input_dir, "*.PNG")
    png_files.extend(glob.glob(png_pattern_upper, recursive=False))
    
    if not png_files:
        print(f"No PNG files found in: {input_dir}")
        return
    
    print(f"Found {len(png_files)} PNG files to convert")
    print(f"Target resolution: {target_width}x{target_height} (8-bit grayscale)")
    print("-" * 50)
    
    processed_count = 0
    error_count = 0
    
    for file_path in png_files:
        try:
            # Open the image
            with Image.open(file_path) as img:
                original_size = img.size
                original_mode = img.mode
                print(f"Processing: {os.path.basename(file_path)} ({original_size[0]}x{original_size[1]}, {original_mode})")
                
                # Convert to 8-bit grayscale (L mode) as required for CK3 terrain masks
                if img.mode != 'L':
                    print(f"  Converting from {img.mode} to 8-bit grayscale")
                    img = img.convert('L')
                
                # Resize the image
                resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                
                # Ensure it's still 8-bit grayscale after resize
                if resized_img.mode != 'L':
                    resized_img = resized_img.convert('L')
                
                # Save to output directory as 8-bit grayscale PNG
                output_filename = os.path.basename(file_path)
                output_path = os.path.join(output_dir, output_filename)
                
                # Save with specific parameters to ensure 8-bit grayscale
                resized_img.save(output_path, 'PNG', optimize=True, bits=8)
                
                print(f"  → Saved: {output_filename} ({target_width}x{target_height}, 8-bit grayscale)")
                processed_count += 1
                
        except Exception as e:
            print(f"  ✗ Error processing {os.path.basename(file_path)}: {str(e)}")
            error_count += 1
    
    print("-" * 50)
    print(f"Conversion complete!")
    print(f"Successfully processed: {processed_count} files")
    if error_count > 0:
        print(f"Errors encountered: {error_count} files")

def convert_png_to_custom_size(input_dir, output_dir, width, height):
    """Convert PNG files to custom resolution"""
    convert_png_files(input_dir, output_dir, width, height)

def main():
    if len(sys.argv) < 3:
        print("CK3 Terrain Mask Converter")
        print("=" * 30)
        print("Usage:")
        print("  python ck3_mask_converter.py <input_folder> <output_folder>")
        print("  python ck3_mask_converter.py <input_folder> <output_folder> <width> <height>")
        print()
        print("Examples:")
        print("  # Convert to TC Sandbox scale (4608x2304)")
        print("  python ck3_mask_converter.py C:\\masks C:\\masks_converted")
        print()
        print("  # Convert to custom size")
        print("  python ck3_mask_converter.py C:\\masks C:\\masks_converted 4096 2048")
        print()
        print("Requirements: pip install Pillow")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder does not exist: {input_folder}")
        sys.exit(1)
    
    # Check for custom dimensions
    if len(sys.argv) >= 5:
        try:
            width = int(sys.argv[3])
            height = int(sys.argv[4])
            print(f"Using custom resolution: {width}x{height}")
            convert_png_to_custom_size(input_folder, output_folder, width, height)
        except ValueError:
            print("Error: Width and height must be integers")
            sys.exit(1)
    else:
        print("Using TC Sandbox scale: 4608x2304")
        convert_png_files(input_folder, output_folder)

if __name__ == "__main__":
    main()
