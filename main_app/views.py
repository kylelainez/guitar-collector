from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar

# Create your views here.
class CreateGuitar(CreateView):
    model = Guitar
    fields = '__all__'

class UpdateGuitar(UpdateView):
    model = Guitar
    fields = '__all__'

class DeleteGuitar(DeleteView):
    model = Guitar
    success_url = '/guitars/'

def home(request):
    return render(request, 'home.html')

def index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})

def detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    return render(request, 'guitars/detail.html', {'guitar': guitar})