from backend.storage.config import port, url
from backend.storage import other
import requests
import pytest

@pytest.fixture
def clear():
    requests.delete(other.CLEAR_URL, json={})


def test_signup(clear):
    request_data = requests.post(other.SIGNUP_URL, json={'name': "Tester One", "email": "dbctesteremail@gmail.com"})
    status = request_data.status_code
    assert (status == 200) # Success

