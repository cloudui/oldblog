from django.urls import path

from .views import HomePageView, PostDetailView, SearchResultsListView, AboutPageView, ZoomLinks

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('classes/', ZoomLinks.as_view(), name='zoom'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
]