from django.shortcuts import render, redirect, get_object_or_404
from app.models import Pessoa
from app.forms import PessoaForm

#Create
#Read
#Update
#Delete

def list(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoa': pessoa})


def create(request):
    form = PessoaForm(request.POST) # request.POST , é informado no method do html
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'create.html', {'form': form})


def update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('list')
    return render(request, 'delete.html', {'pessoa': pessoa})
