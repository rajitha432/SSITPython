import string

import pytest
import requests
import json
import random
from confest import *


@pytest.mark.smoke
@pytest.mark.usefixtures("get_token")
def test_get_users_valid(get_token):
    url = "https://gorest.co.in/public/v2/users"
    headers = get_token
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert len(result) > 0
    for data in result:
        assert data["id"] is not None
        assert data["name"] is not None
        assert data["email"] is not None
        assert data["gender"] is not None
        assert data["status"] is not None

@pytest.mark.usefixtures("get_token")
def test_get_user_invalid_url(get_token):
    url = "https://gorest.co.in/public/v2/users767"
    headers = get_token
    response = requests.get(url, headers=headers)
    assert response.status_code == 404

@pytest.mark.smoke
@pytest.mark.usefixtures("get_token")
def test_get_user_detail(get_token):
    url = "https://gorest.co.in/public/v2/users/683371"
    headers = get_token
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    result = response.json()
    assert result["id"] == 683371
    # assert result["name"] == "Divjot Bhattathiri"
    # assert result["email"] == "bhattathiri_divjot@bayer.io"
    # assert result["gender"] == "female"
    # assert result["status"] == "inactive"

@pytest.mark.smoke
@pytest.mark.usefixtures("get_token")
def test_create_user(get_token):
    url = "https://gorest.co.in/public/v2/users"
    temp = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=10))
    email = temp +"@gmil.com"
    payload = json.dumps({
        "name": "raj",
        "gender": "male",
        "email": email,
        "status": "Active"
    })
    header = get_token
    response = requests.post(url,headers=header,data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["id"] is not None
    assert result["name"] == "raj"
    assert result["gender"] == "male"
    assert result["email"] == email
    assert result["status"] == "active"