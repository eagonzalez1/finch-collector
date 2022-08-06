from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })