from django.urls import path
from agents.views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name="agent-list"),  # agent list view link
    path('<int:pk>/', AgentDetailView.as_view(),
         name="agent-detail"),  # agent detail View
    path('<int:pk>/update', AgentUpdateView.as_view(),
         name="agent-update"),  # update link
    path('<int:pk>/delete', AgentDeleteView.as_view(),
         name="agent-delete"),  # delete link
    path('create/', AgentCreateView.as_view(),
         name="agent-create"),  # agent create link

]
