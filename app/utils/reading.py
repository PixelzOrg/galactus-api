"""
reading.py

This file contains all of our reading methods
"""

def read_glb_file_as_bytes(file_path):
    try:
        with open(file_path, 'rb') as glb_file:
            glb_bytes = glb_file.read()
        return glb_bytes
    except FileNotFoundError:
        print(f"Error: GLB file not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def read_gif_file_as_bytes(file_path):
    try:
        with open(file_path, 'rb') as gif_file:
            gif_bytes = gif_file.read()
        return gif_bytes
    except FileNotFoundError:
        print(f"Error: GIF file not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
