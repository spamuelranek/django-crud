from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from snacks.models import Snack
from django.urls import reverse_lazy

class HomePageView(TemplateView):
  template_name = "home.html"

class TestPageView(TemplateView):
  template_name = "test.html"

class SnackListView(ListView):
  template_name = "snack_list.html"
  model = Snack 

class SnackDetailView(DetailView):
  teplate_name = "snack_detail.html"
  model = Snack

class SnackCreatView(CreateView):
  template_name = "snack_create.html"
  model = Snack
  fields = ['title','purchaser','description']

class SnackUpdateView(UpdateView):
  template_name = "snack_update.html"
  model = Snack
  fields = ['title', 'description']

class SnackDeleteView(DeleteView):
  template_name = "snack_delete.html"
  model = Snack
  success_url = reverse_lazy("snack_list")