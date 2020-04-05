from django.shortcuts import render
from django.http import HttpResponse

# render function takes request as first argument, and template name as second argument
# third optional argument is 'context' which is used to pass information on to our template

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
# Create your views here.
