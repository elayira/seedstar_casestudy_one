from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import EmailList
from .forms import EmailListForm


class DisplayEmailList(ListView):
    model = EmailList
    template_name = "emaillist/display.html"


class AddEmail(CreateView):
    form_class = EmailListForm
    success_url = reverse_lazy("emaillist:display")
    template_name = "emaillist/add.html"

