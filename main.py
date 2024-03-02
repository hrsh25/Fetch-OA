from fastapi import FastAPI, HTTPException
from models import Receipt
from receipt_processing import ReceiptProcessor
import uuid

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0"
)

# Simulated in-memory database for storing receipts
db = {}

@app.post("/receipts/process", response_model=dict)
async def process_receipt(receipt: Receipt):
    """
    Endpoint to process a receipt. Validates the receipt data, assigns a unique ID, and stores it in the database.
    Args:
        receipt (Receipt): The receipt data sent by the client.
    Returns:
        dict: A dictionary containing the unique ID of the processed receipt.
    """
    # Generate a unique identifier for the new receipt
    receipt_id = str(uuid.uuid1())
    # Store the receipt in the "database" using the generated ID
    db[receipt_id] = receipt
    # Return the ID to the client
    return {"id": receipt_id}

@app.get("/receipts/{id}/points")
async def get_points(id: str):
    """
    Endpoint to retrieve the points awarded for a processed receipt.
    Args:
        id (str): The unique ID of the receipt.
    Returns:
        dict: A dictionary containing the number of points awarded to the receipt.
    Raises:
        HTTPException: If no receipt with the provided ID is found.
    """
    # Attempt to retrieve the receipt from the database
    receipt = db.get(id)
    if not receipt:
        # If not found, return a 404 error
        raise HTTPException(status_code=404, detail="No receipt found for that id")
    
    # Calculate points for the retrieved receipt
    processor = ReceiptProcessor()
    points = processor.calculate_points(receipt)
    # Return the points in the response
    return {"points": points}
