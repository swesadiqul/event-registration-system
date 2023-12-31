from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)