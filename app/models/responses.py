"""
responses.py

This file contains all of our API responses to our client
"""
import base64

class GenerationResponse:
    def __init__(
            self, 
            status, 
            glb_filename, 
            glb_content_type, 
            glb_bytes, 
            gif_filename, 
            gif_content_type, 
            gif_bytes
          ):
        self.status = status
        self.data = {
            "glb_file": {
                "filename": glb_filename,
                "content_type": glb_content_type,
                "data": base64.b64encode(glb_bytes).decode('utf-8')
            },
            "gif_file": {
                "filename": gif_filename,
                "content_type": gif_content_type,
                "data": base64.b64encode(gif_bytes).decode('utf-8')
            }
        }