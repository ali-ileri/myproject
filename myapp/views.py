from django.shortcuts import render, redirect
from .forms import KaynakForm
from .models import Kaynak

def kaynak_list(request):
    kaynaklar = Kaynak.objects.all()
    form = KaynakForm()
    
    if request.method == 'POST':
        form = KaynakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kaynak_list')
    
    return render(request, 'kaynak_list.html', {'kaynaklar': kaynaklar, 'form': form})

def kaynak_edit(request, pk):
    kaynak = Kaynak.objects.get(pk=pk)
    form = KaynakForm(instance=kaynak)
    
    if request.method == 'POST':
        form = KaynakForm(request.POST, instance=kaynak)
        if form.is_valid():
            form.save()
            return redirect('kaynak_list')
    
    return render(request, 'kaynak_list.html', {'kaynaklar': Kaynak.objects.all(), 'form': form})

def kaynak_delete(request, pk):
    kaynak = Kaynak.objects.get(pk=pk)
    kaynak.delete()
    return redirect('kaynak_list')
