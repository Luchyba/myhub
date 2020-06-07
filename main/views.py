from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(request):
    return render(request, 'home.html', )


def event(request):
    return render(request, 'coc.html', )


def community(request):
    return render(request, 'services.html', )


def team(request):
    return render(request, 'pricing.html', )


def about(request):
    return render(request, 'about.html', )


def camp(request):
    return render(request, 'blog.html', )


def volunteer(request):
    return render(request, 'volunteer.html', )


def project(request):
    return render(request, 'project.html', )


def incubate(request):
    return render(request, 'incubator.html', )


def it4gh(request):
    return render(request, 'it4gh.html', )

def ccoc(request):
    return render(request, 'ccoc.html', )
