from django.urls import path
from .views import ScraperServiceView
urlpatterns = [
    path('scrape', ScraperServiceView.as_view()),
]
