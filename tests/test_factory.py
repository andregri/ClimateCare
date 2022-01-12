import sys

sys.path.append('./') # Append the current folder that contains app.py

from app import create_app


def test_config():
    response = create_app().test_client().get('/')
    assert response.status_code == 200