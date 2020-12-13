from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar

# Create your views here.
class CreateGuitar(CreateView):
    model = Guitar
    fields = '__all__'

def home(request):
    return render(request, 'home.html')

def index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})