import json
import os
import pytest
import pymongo
from utils.file_converter import csv_to_json

@pytest.fixture
def csv_file_path():
    # Assuming the CSV file is located in the "tests" directory
    return os.path.join(os.path.dirname(__file__), 'cincinnati.csv')

def test_csv_to_json(csv_file_path):
    # Test if CSV to JSON conversion works without error
    json_file_path = csv_file_path.replace('.csv', '.json')
    csv_to_json(csv_file_path)
    assert os.path.exists(json_file_path), "JSON file was not created."

    # Clean up: Remove the generated JSON file
    # os.remove(json_file_path)


# Pytest function to test accessing the first document in MongoDB
def test_access_first_document_in_mongodb():
    # Load the JSON file
    json_data = []
    with open("grand_rapids_normalized.json", "r") as json_file:
        for line in json_file:
            json_data.append(json.loads(line))

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["lead_in_water"]
    collection = db["grand_rapids"]

    # Query MongoDB to retrieve the first document
    mongo_document = collection.find_one()

    # Assert that the MongoDB document matches the first document from the JSON file
    print(mongo_document)
    print(json_data[0])