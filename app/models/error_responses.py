"""
error_responses.py

This file contains all of our error responses to our client
"""

def create_error_response(method_name, error_message, additional_info=None):
    error_response = {
        "status": "error",
        "message": "An error occurred during method execution.",
        "error_details": {
            "method": method_name,
            "error_message": error_message
        }
    }
    
    if additional_info:
        error_response["error_details"]["additional_info"] = additional_info
    
    return error_response