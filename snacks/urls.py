from django.urls import path
from snacks.views import SnackCreatView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView, TestPageView


urlpatterns = [
  path("",SnackListView.as_view(), name = "snack_list"),
  path("test/", TestPageView.as_view(), name = "test"),
  path("<int:pk>/",SnackDetailView.as_view(), name = "snack_detail"),
  path("create/", SnackCreatView.as_view(), name = "snack_create"),
  path("<int:pk>/delete/", SnackDeleteView.as_view(), name = "snack_delete"),
  path("<int:pk>/update/", SnackUpdateView.as_view(), name = "snack_update"),
  ]