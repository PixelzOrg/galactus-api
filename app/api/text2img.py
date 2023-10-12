"""
model_loaders.py

This file contains our Text2Image API 
"""
import os
import torch
from PIL import Image
from typing import List
from diffusers import DiffusionPipeline
from dotenv import load_dotenv
load_dotenv()
class Text2Image:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipe = DiffusionPipeline.from_pretrained(
            "openai/shap-e", 
            torch_dtype=torch.float16, 
            variant="fp16", 
            use_auth_token=os.getenv("HUGGING_FACE"),
        )
        self.pipe = self.pipe.to(self.device)
        self.guidance_scale = 15.0

    def generate_mesh_from_prompt(
            self, 
            prompt: str, 
            frame: int = 256,
            inference_steps: int = 64,
        ) -> List[Image.Image]:
        """
        Generate a mesh as glb from the given prompt

        :param prompt (str): The text prompt to generate a mesh from
        :param guidance_scale (float): The amount of guidance to use
        :return: 
        """
        print("received request")
        mesh = self.pipe(
            prompt,
            guidance_scale=self.guidance_scale,# type: ignore
            num_inference_steps=inference_steps,
            frame_size=frame, # type: ignore
            output_type="mesh",).images
        return mesh
