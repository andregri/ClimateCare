from app import create_app


def test_config():
    response = create_app().test_client().get('/')
    assert response.status_code == 200