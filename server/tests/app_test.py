import pytest
import json
import requests


@pytest.mark.usefixtures("restart_api")
def test_get_algorithms(api_url, session: requests.Session):
    r = session.get(api_url + "/algorithms")
    assert r.status_code == 200
    assert "algorithms" in r.json()


@pytest.mark.usefixtures("restart_api")
def test_post_encode_eliasgamma(api_url, session: requests.Session):
    data = {"algorithm": "eliasgamma", "word": "test"}
    r = session.post(
        api_url + "/encode",
        data=json.dumps(data)
    )
    assert r.status_code == 200
    assert "codeword" in r.json()
    assert r.json()["codeword"] == [
        "0000001110100",
        "0000001100101",
        "0000001110011",
        "0000001110100"
    ]
