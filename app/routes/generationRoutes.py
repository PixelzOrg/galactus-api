"""
generate_route.py

API routes for generating meshes
"""
from flask import Response, request, Blueprint
from app.services.generationService import MeshService
from app.middleware.authentication import authentication_middleware

generate = Blueprint("generate", __name__)
mesh_service = MeshService()

@generate.route("/generate_mesh_from_prompt", methods=["POST"])
@authentication_middleware
def generate_glb_from_prompt() -> Response:
    """
    Generate a mesh as glb from the given prompt

    :param prompt (any): The text prompt to generate a mesh from
    :return (json): response containing the generated mesh as glb
    :raises: 500 error if an error occurs
    """
    try:
        prompt = request.json["prompt"]
        mesh, gif = mesh_service.generate_mesh_glb_from_prompt(prompt)
        return Response(
            mesh,
            gif,
            mimetype="model/gltf-binary",
            headers={
                "Content-Disposition": f'attachment;filename={prompt}.glb'
            },
            status=200
        )
    except Exception as error:
        return Response(
            error,
            mimetype="application/json",
            status=500
        )

@generate.route("/generate_mesh_from_image", methods=["POST"])
@authentication_middleware
def generate_mesh_from_image() -> Response:
    """
    Generate a mesh as glb from the given image

    :param prompt (any): The text prompt to generate a mesh from
    :return (json): response containing the generated mesh as glb
    :raises: 500 error if an error occurs
    """
    try:
        prompt = request.json["prompt"]
        buffer, gif = mesh_service.generate_mesh_glb_from_image(prompt)
        return Response(
            buffer.read(),
            mimetype="model/gltf-binary",
            headers={
                "Content-Disposition": f'attachment;filename={prompt}.glb'
            },
            status=200
        )
    except Exception as error:
        return Response(
            error,
            mimetype="application/json",
            status=500
        )