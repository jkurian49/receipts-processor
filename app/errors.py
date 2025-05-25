from flask import jsonify, Response
from typing import Any, Tuple

def handle_request_validation_error(error: Any) -> Tuple[Response, int]:
    error_response = {
        "error": "Invalid request payload.",
        "message": error.message,
        "path": list(error.path),
    }
    return jsonify(error_response), 400

def handle_404(error: Any) -> Tuple[Response, int]:
    return jsonify({"error": "Resource not found"}), 404

def handle_500(error: Any) -> Tuple[Response, int]:
    return jsonify({"error": "Internal server error"}), 500
