from django.shortcuts import render, HttpResponse

def home(request):
  return HttpResponse('Hello, Word !')

def about(request):
  return HttpResponse('La page About')

def index(request):
  return render(request, 'base.html')