from django.shortcuts import render

posts = [
    {
        'author': 'GregM',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 5 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 6 2020'
    }
]

# render function takes request as first argument, and template name as second argument
# third optional argument is 'context' which is used to pass information on to our template

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.
