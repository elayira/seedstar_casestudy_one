from django.urls import path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from seedstar_casestudy_one.emaillist.views import (
    DisplayEmailList,
    AddEmail
)

app_name = "emaillist"
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("list", view=DisplayEmailList.as_view(), name="display"),
    path("add", view=AddEmail.as_view(), name="add"),
]
