from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Accessory
from .forms import MaintenanceForm

# Create your views here.
class CreateGuitar(CreateView):
    model = Guitar
    fields = ['brand', 'model', 'guitar_type', 'price', 'description']

class UpdateGuitar(UpdateView):
    model = Guitar
    fields = ['brand', 'model', 'guitar_type', 'price', 'description']

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
    accessory_nin_guitar = Accessory.objects.exclude(id__in = guitar.accessories.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'guitars/detail.html', {
        'guitar': guitar,
        'maintenance_form': maintenance_form,
        'accessories': accessory_nin_guitar
        })
        
def add_maintenance(request, guitar_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.guitar_id = guitar_id
        new_maintenance.save()
    return redirect('detail', guitar_id = guitar_id)

def add_accessory(request, guitar_id):
    Guitar.objects.get(id=guitar_id).accessories.add(request.POST['accessories'])
    return redirect('detail', guitar_id=guitar_id)

def remove_accessory(request, guitar_id, accessory_id):
    Guitar.objects.get(id=guitar_id).accessories.remove(accessory_id)
    return redirect('detail', guitar_id=guitar_id)


class AccessoriesList(ListView):
    model = Accessory

class AccessoriesDetail(DetailView):
    model = Accessory

class AccessoriesCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoriesUpdate(UpdateView):
    model = Accessory
    fields = '__all__'

class AccessoriesDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'