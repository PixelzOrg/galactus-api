"""
util.py

This file contains all of our utility functions
"""
import trimesh
from diffusers.utils import export_to_ply

def convert_mesh_to_glb(mesh: trimesh.Trimesh) -> bytes:
    """
    Convert a mesh to a glb file

    :param mesh (trimesh.Trimesh): The mesh to convert
    :return: The glb file
    """
    