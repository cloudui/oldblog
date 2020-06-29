from django.urls import path

from .views import HomePageView, PostDetailView, SearchResultsListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
]