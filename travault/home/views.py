from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page. """
    return render (request, 'home/index.html')

def terms_of_service(request):
    """ A view to return the Terms of Service page. """
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    """ A view to return the Privacy Policy page. """
    return render(request, 'privacy_policy.html')