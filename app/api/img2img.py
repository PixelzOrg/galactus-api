"""
img2img.py

This module contains the Image2Image class, 
which is used to generate a mesh from an image
"""

import torch
import os
from PIL import Image
from dotenv import load_dotenv
from diffusers import DiffusionPipeline
load_dotenv()
class Image2Image:
    def __init__(self):
        self.pipe = DiffusionPipeline.from_pretrained(
            "openai/shap-e-img2img", 
            torch_dtype=torch.float16, 
            variant="fp16",
            use_safetensors=True,
            use_auth_token=os.getenv("HUGGING_FACE"),
        ).to("cuda")
    
    def generate_mesh_from_image(
            self,
            image: Image,
            guidance_scale: float
    ) -> torch.Tensor:
        """
        Generate a mesh from the given image

        :param image (Image): The image to generate a mesh from
        :param guidance_scale (float): The amount of guidance to use
        :return (tensor.Tensor): the generated mesh
        """
        mesh = self.pipe(
            image,
            guidance_scale=guidance_scale,
            num_inference_steps=64,
            frame_size=256,
            output_type="mesh",).images
        return mesh