from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'ildan/index.html')

def find_tutor(request):
  return render(request, 'ildan/find_tutor.html')

def tutor_detail(request):
  return render(request, 'ildan/tutor_detail.html')

def tutor_detail2(request):
  return render(request, 'ildan/tutor_detail2.html')