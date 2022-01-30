from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from django_weasyprint import WeasyTemplateResponseMixin

from .forms import PersonForm
from .mixins import SearchMixin
from .models import Person


class PersonListView(SearchMixin, ListView):
    model = Person
    paginate_by = 10


class PersonDetailView(DetailView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('crm:person_list')


class PersonReport(WeasyTemplateResponseMixin, ListView):
    model = Person
    template_name = 'report/person_report.html'

    def get_pdf_filename(self):
        at = datetime.now().strftime('%Y-%m-%d-%H-%M')
        return f'report_{at}.pdf'
