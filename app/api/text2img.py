"""
model_loaders.py

This file contains our Text2Image API 
"""
import os
import torch
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
            use_safetensors=True,
            use_auth_token=os.getenv("HUGGING_FACE"),
        )
        self.pipe = self.pipe.to(self.device)

    def generate_mesh_from_prompt(
            self, 
            prompt: str, 
            guidance_scale: float
        ) -> torch.Tensor:
        """
        Generate a mesh as glb from the given prompt

        :param prompt (str): The text prompt to generate a mesh from
        :param guidance_scale (float): The amount of guidance to use
        :return: 
        """
        mesh = self.pipe(
            prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=64,
            frame_size=256,
            output_type="mesh",).images
        return mesh
