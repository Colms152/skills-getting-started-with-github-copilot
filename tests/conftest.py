import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


BASE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture()
def client():
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(BASE_ACTIVITIES))

    with TestClient(app_module.app) as test_client:
        yield test_client
