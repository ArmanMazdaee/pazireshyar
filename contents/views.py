from django.views.generic import DetailView

from .models import University


class University(DetailView):
    template_name = 'contents/university.html'
    model = University
