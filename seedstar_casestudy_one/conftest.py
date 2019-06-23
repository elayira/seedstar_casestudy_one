import pytest
from django.conf import settings
from django.test import RequestFactory

from seedstar_casestudy_one.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath



@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
