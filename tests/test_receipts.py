import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app({
        "TESTING": True
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_process_valid_receipt(client):
    valid_payload = {
      "retailer": "Target",
      "purchaseDate": "2022-01-01",
      "purchaseTime": "13:01",
      "items": [
        {
          "shortDescription": "Mountain Dew 12PK",
          "price": "6.49"
        },{
          "shortDescription": "Emils Cheese Pizza",
          "price": "12.25"
        },{
          "shortDescription": "Knorr Creamy Chicken",
          "price": "1.26"
        },{
          "shortDescription": "Doritos Nacho Cheese",
          "price": "3.35"
        },{
          "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
          "price": "12.00"
        }
      ],
      "total": "35.35"
    }
    
    response = client.post("/api/v1/receipts/process", json=valid_payload)
    
    assert response.status_code == 200
    data = response.get_json()
    assert "id" in data

def test_process_invalid_receipt_missing_field(client):
    invalid_payload = {
      "retailer": "Target",
      "purchaseDate": "2022-01-01",
      "purchaseTime": "13:01",
      "items": [
        {
          "shortDescription": "Mountain Dew 12PK",
          "price": "6.49"
        },{
          "shortDescription": "Emils Cheese Pizza",
          "price": "12.25"
        },{
          "shortDescription": "Knorr Creamy Chicken",
          "price": "1.26"
        },{
          "shortDescription": "Doritos Nacho Cheese",
          "price": "3.35"
        },{
          "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
          "price": "12.00"
        }
      ]
    }
    
    response = client.post("/api/v1/receipts/process", json=invalid_payload)
    
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Invalid request payload."
    assert data["message"] == "'total' is a required property"

def test_get_points_valid_id(client):
    payload = {
        "retailer": "Target",
        "purchaseDate": "2024-11-10",
        "purchaseTime": "15:30",
        "items": [
            {"shortDescription": "Cereal", "price": "4.99"},
            {"shortDescription": "Milk", "price": "2.99"}
        ],
        "total": "7.98"
    }
    process_response = client.post("/api/v1/receipts/process", json=payload)
    receipt_id = process_response.get_json()["id"]

    response = client.get(f"/api/v1/receipts/{receipt_id}/points")
    assert response.status_code == 200
    data = response.get_json()
    assert "points" in data

def test_get_points_invalid_id(client):
    response = client.get("/api/v1/receipts/invalid-id/points")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Resource not found"


