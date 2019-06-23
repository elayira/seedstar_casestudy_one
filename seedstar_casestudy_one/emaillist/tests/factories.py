from factory import DjangoModelFactory, Faker, post_generation


class EmailListFactory(DjangoModelFactory):

    email = Faker("email")
    name = Faker("name")

    class Meta:
        model = "emaillist.EmailList"
        django_get_or_create = ["email"]
