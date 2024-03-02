from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_receipt():
    receipt_data = {
        "retailer": "TestStore",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Item1", "price": "1.00"},
            {"shortDescription": "Item2", "price": "2.00"}
        ],
        "total": "3.00"
    }
    response = client.post("/receipts/process", json=receipt_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_points():
    receipt_data = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            }
        ],
        "total": "9.00"
    }
    response = client.post("/receipts/process", json=receipt_data)
    assert response.status_code == 200
    assert "id" in response.json()
    receipt_id = response.json()['id']
    get_response = client.get(f"/receipts/{receipt_id}/points")
    assert get_response.status_code == 200
    points = get_response.json()['points']
    assert points == 109

def test_get_points_nonexistent_receipt():
    response = client.get("/receipts/1/points")
    assert response.status_code == 404
