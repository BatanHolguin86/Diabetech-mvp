import os
import json
from pathlib import Path
import pytest

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app, load_data

@pytest.fixture
def client(tmp_path):
    data_file = tmp_path / 'data.json'
    os.environ['DATA_FILE'] = str(data_file)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    os.environ.pop('DATA_FILE')

def test_home_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'DiabeTech' in resp.data

def test_registro(client):
    resp = client.post('/registro', data={'tipo': 'glucosa', 'valor': '100'}, follow_redirects=True)
    assert resp.status_code == 200
    data = load_data()
    assert '100' in data['glucosa']
    assert b'Registro agregado' in resp.data

def test_registro_invalid(client):
    resp = client.post('/registro', data={'tipo': 'glucosa', 'valor': ''}, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Tipo o valor inv\xc3\xa1lido' in resp.data
