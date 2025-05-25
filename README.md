# Receipt Processor

A Flask-based API for processing receipts and calculating reward points based on receipt data.

## Features

- Accepts receipt data via a POST endpoint.
- Calculates points based on retailer, total, items, purchase date, and time.
- Returns a unique ID for each processed receipt.
- Allows querying points for a given receipt ID.

## Setup & Running the Application

This project is intended to be run using Docker.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jkurian49/receipts-processor.git
   cd receipt-processor
   ```

2. **Build and run the Docker container:**

   ```bash
   docker build -t receipt-processor .
   docker run --rm -p 5000:5000 -e FLASK_ENV=development receipt-processor
   ```

The API will be available at `http://localhost:5000/api/v1/receipts`.

## Running Tests

To run the test suite inside the Docker container:

```bash
docker run --rm receipt-processor pytest
```

Or, if you prefer to run tests locally (requires Python and dependencies installed):

```bash
pytest
```

## API Endpoints

### `POST /api/v1/receipts/process`

Process a receipt and receive a unique ID.

**Request Body:**  
JSON matching the required schema.

**Response:**

```json
{ "id": "<receipt-id>" }
```

### `GET /api/v1/receipts/<id>/points`

Retrieve points for a processed receipt.

**Response:**

```json
{ "points": <points> }
```

## Project Structure

- `app/receipts.py` - Main API endpoints and logic.
- `app/utils.py` - Utility functions for point calculations.
- `app/schemas.py` - JSON schema for receipt validation.

## License

MIT License.
