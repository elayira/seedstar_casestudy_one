import pytest

from seedstar_casestudy_one.emaillist.forms import EmailListForm
from seedstar_casestudy_one.emaillist.tests.factories import EmailListFactory

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    def test_clean_username(self):
        named_email = EmailListFactory.build()

        form = EmailListForm(
            {
                "name": named_email.name,
                "password1": named_email.email
            }
        )

        assert form.is_valid()
        assert form.clean_email() == named_email.email

        # Creating a named email.
        form.save()

        # The named email with email params already exists,
        # hence cannot be created.
        form = EmailListForm(
            {
                "name": named_email.name,
                "password1": named_email.email
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors
