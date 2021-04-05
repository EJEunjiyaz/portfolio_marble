from django.shortcuts import render


# Create your views here.
def index_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")


def portfolio_view(request):
    return render(request, "portfolio.html")


def about_view(request):
    return render(request, "about.html")
