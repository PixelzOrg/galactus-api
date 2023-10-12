"""
generation_service.py

This service layer is responsible for validating the prompt
and calling our meshAPI and returning a mesh.
"""
import io
from PIL import Image
from typing import Any
from diffusers.utils import export_to_gif
from app.utils.convert import convert_mesh_to_glb
from app.utils.reading import read_file_as_bytes
from app.api.text2img import Text2Image
from app.api.img2img import Image2Image
from app.models.constants import (
    PROMPT_LENGTH_ERROR,
    PROMPT_TYPE_ERROR
)

class MeshService:
    """
    This class will validate the prompt and call the meshAPI
    to generate a mesh from the prompt.
    """
    def __init__(self):
        self.text2image = Text2Image()
        self.image2image = Image2Image()

    def generate_mesh_glb_from_image(self, name: str, image: Image.Image) -> io.BytesIO:
        """
        After validation we call the image2image model

        :param prompt (str): The text prompt to generate a mesh from
        :return: A tuple containing the mesh and the filename
        """
        try:
            self.validate_image(image)
            mesh = self.image2image.generate_mesh_from_image(image)

            glb_bytes = read_file_as_bytes(convert_mesh_to_glb(mesh, name))
            gif_bytes = read_file_as_bytes(export_to_gif(mesh[0], f"{name}.gif"))
            return glb_bytes, gif_bytes

        except Exception as error:
            # TODO: Add json response to client
            raise error
    
    def generate_mesh_glb_from_prompt(self, prompt: str,) -> io.BytesIO:
        """
        After validation we call the text2image model

        :param prompt (str): the text prompt to generate a mesh from
        :return: A tuple containing the mesh and the filename
        """
        try:
            self.validate_prompt(prompt)
            print("validated")
            mesh = self.text2image.generate_mesh_from_prompt(prompt)

            glb_bytes = read_glb_file_as_bytes(convert_mesh_to_glb(mesh, prompt))
            gif_bytes = read_gif_file_as_bytes(export_to_gif(mesh[0], f"{prompt}.gif"))
            return glb_bytes, gif_bytes
        
        except Exception as error:
            # TODO: Add json response to client
            raise error
        
    def validate_image(self, image: Image.Image) -> None:
        """
        We need to validate the image 
        before we can generate a mesh from it.

        :param image (Image): The image to validate
        :raises TypeError: If the image is not a PIL Image
        """
        pass
            
    def validate_prompt(self, prompt: Any) -> None:
        """
        We need to validate the prompt 
        before we can generate a mesh from it.

        :param prompt (any): The text prompt to validate
        :raises TypeError: If the prompt is not a string
        :raises ValueError: If the prompt is longer than 50 characters
        """
        if not isinstance(prompt, str):
            # TODO: Add json response to client
            raise TypeError(PROMPT_TYPE_ERROR)

        if len(prompt) > 50:
            # TODO: Add json response to client
            raise ValueError(PROMPT_LENGTH_ERROR)