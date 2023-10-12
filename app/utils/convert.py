"""
convert.py

This file holds all of our conversion methods
"""

import trimesh
from typing import List
from PIL import Image
from diffusers.utils import export_to_ply

def convert_mesh_to_glb(mesh: List[Image.Image], prompt: str):
    """
    Convert a mesh to a glb

    :param mesh (List[Image.Image]): The mesh to convert
    :return: A glb file
    """
    glb = export_to_ply(mesh[0], f"{prompt}.glb")
    trimesh = trimesh.load(glb)
    return trimesh.export(f"{prompt}.glb", file_type="glb")