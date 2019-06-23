import pytestfrom django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_list():
    assert resolve(f"/list").view_name == "emaillist:display"
    assert reverse("emaillist:display") == "/list"


def test_add():
    assert reverse("emaillist:add") == "/add"
    assert resolve("/add").view_name == "emaillist:add"
