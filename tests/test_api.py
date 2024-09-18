import pytest
from app import app, products

def test_get_products():
    response = app.test_client().get('/products')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 2
    assert data[0]['Name'] == 'Gago'