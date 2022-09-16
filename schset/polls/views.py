from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,sch")
# Create your views here.
