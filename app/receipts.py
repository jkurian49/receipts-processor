import logging
from flask import Blueprint, jsonify, request
from jsonschema import validate, ValidationError
import uuid
from app.utils import *
from app.schemas import RECEIPT_SCHEMA
from app.errors import handle_request_validation_error, handle_404, handle_500
from typing import Dict, Any

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

bp = Blueprint('receipts', __name__, url_prefix='/api/v1/receipts')

# Register error handlers
bp.register_error_handler(ValidationError, handle_request_validation_error)
bp.register_error_handler(404, handle_404)
bp.register_error_handler(500, handle_500)

receipt_points: Dict[str, int] = {}

@bp.route('/process', methods=["POST"])
def process() -> Any:
    try:
        validate(instance=request.json, schema=RECEIPT_SCHEMA)
    except ValidationError as e:
        logger.error(f"Validation error: {e.message} | Data: {request.json}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error during validation: {e}")
        raise
    points = calculate_points(request.json)
    new_id = str(uuid.uuid4())
    receipt_points[new_id] = points
    logger.info(f"Processed receipt. ID: {new_id}, Points: {points}")
    return jsonify({'id': new_id})

@bp.route('/<id>/points', methods=["GET"])
def getPoints(id: str) -> Any:
    if id not in receipt_points:
        logger.warning(f"Receipt ID not found: {id}")
        return handle_404(None)
    logger.info(f"Fetched points for ID: {id}")
    return jsonify({'points': receipt_points[id]})