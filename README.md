# Fetch-OA

## FastAPI Receipt Processor

This FastAPI application is designed to process receipts and calculate points based on predefined rules. It provides a RESTful API for submitting receipts and retrieving the calculated points based on various criteria such as the retailer name, total amount, items count, item descriptions, purchase date, and purchase time.

## Features

- Process receipt data via a REST API.
- Calculate points based on retailer name, total amount, items count, item descriptions, purchase date, and purchase time.
- Retrieve points awarded for submitted receipts using a unique ID.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/hrshvora/Fetch-OA.git
    cd Fetch-OA
    ```

2. **Build and Run with Docker Compose**

    ```bash
    docker-compose up --build
    ```

This command builds the Docker image and starts the container(s) as defined in the `docker-compose.yml`. The `--build` flag ensures the image is rebuilt if necessary.

### Usage

#### Process Receipts

Submit receipt data for processing and receive a unique ID for the receipt:

```bash
curl -X 'POST' \
  'http://localhost/receipts/process' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Item 1",
      "price": "5.00"
    }
  ],
  "total": "5.00"
}'
```

#### Get points

Retrieve the points awarded for a processed receipt using its unique ID:

```bash
curl -X 'GET' \
  'http://localhost/receipts/{id}/points' \
  -H 'accept: application/json'
```

Replace `{id}` with the ID returned by the POST request when processing a receipt.

### API Documentation

Access the auto-generated Swagger UI documentation at `http://localhost/docs`. This page provides detailed information about the API endpoints, including the expected request formats and available responses. You can also try the APIs here.

### Running Tests

To run the automated tests for this project, use the following command:

```bash
docker exec -it <container_name> pytest
```
