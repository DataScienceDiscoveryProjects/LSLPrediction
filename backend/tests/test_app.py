import pytest
from app import app


@pytest.fixture
def client():
    # Create a test client using the Flask application context
    with app.app.test_client() as client:
        yield client


def test_get_data_for_address(client):
    # Test retrieving data for a valid address
    address = '2240 Michigan St NE'
    response = client.get(f'/api/getPropertyByAddress?address={address}')
    assert response.status_code == 200
    data = response.json
    assert data['abbreviatedAddress'] == address
    print(data)


def test_invalid_address(client):
    # Test handling of invalid address
    address = 'Invalid Address'
    response = client.get(f'/api/getPropertyByAddress?address={address}')
    assert response.status_code == 404
    error_message = response.json['error']
    assert error_message == 'Property not found'