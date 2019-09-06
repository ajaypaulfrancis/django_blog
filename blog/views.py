from django.shortcuts import render

posts = [
    {
        'author': 'AJ Paul',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'


    },
    {

        'author': 'Sid Saklani',
        'title': 'Learning Ansible',
        'content': 'second post content',
        'date_posted': 'August 28, 2018'




    }


]



def home(request):
    context = {
        'posts': posts

    }
    return render(request, 'blog/home.html', context)

# Create your views here.
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
