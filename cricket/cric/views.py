from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def sandeep_sharma(request):
    return render(request, "sandeep_sharma.html")

def amit_mishra(request):
    return render(request, "amit_mishra.html")

def travis_head(request):
    return render(request, "travis_head.html")