import pytest
from confmodules import load_modules

load_modules()

import time
import requests
from pathlib import Path
from requests.exceptions import ConnectionError


@pytest.fixture
def api_url():
    return f"http://localhost:8080"


def wait_for_webapp_to_come_up(api_url):
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return requests.get(api_url)
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail("API never came up")


@pytest.fixture
def restart_api(api_url):
    (Path(__file__).parent / "../src/app.py").touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up(api_url)


@pytest.fixture
def session():
    with requests.Session() as s:
        s.headers.update({"Content-type": "application/json"})
        yield s
