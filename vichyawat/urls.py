from django.urls import path

# importing views from views..py
from .views import index_view, portfolio_view, about_view

urlpatterns = [
    path('', index_view),
    path('index.html', index_view),
    path('portfolio.html', portfolio_view),
    path('about.html', about_view),
]