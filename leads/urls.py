from django.urls import path

from leads.views import leadListView, leadDetailView, leadCreateView, leadUpdateView, leadDeleteView


app_name = "leads"

urlpatterns = [
    path('', leadListView.as_view(), name="lead-list"),  # lists all leads
    path('<int:pk>/', leadDetailView.as_view(), name="lead-detail"),  # lists
    path('<int:pk>/update/', leadUpdateView.as_view(), name="lead-update"),  # lead update
    path('<int:pk>/delete', leadDeleteView.as_view(), name="lead-delete"),  # lead Deletion
    path('create/', leadCreateView.as_view(), name="lead-create"),
]
