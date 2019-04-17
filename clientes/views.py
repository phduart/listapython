from django.shortcuts import redirect
from django.shortcuts import render
from clientes.models import Cliente
from django.http import HttpResponse



def index(request): 
	return render(request, 'index.html', {'clientes' : Cliente.objects.all()})

def listaMedia(request):
	return render(request, 'lista.html', {'clientes' : Cliente.objects.raw('SELECT * FROM clientes_cliente WHERE vl_total > 560 AND id > 1500 AND id < 2700 ORDER BY vl_total ASC;')})


def exibir(request, cliente_id):
	cliente = Cliente.objects.get(id=cliente_id)
	return render(request, 'cliente.html', { "cliente" : cliente})


def salvar(request):
	form = (request.POST)
	perfil = Cliente(id=form['id'],
					cpf_cnpj=form['cpf_cnpj'],
					nm_costume=form['nm_costume'],
					is_active=form['is_active'],
					vl_total=form['valor'])
	perfil.save()
	return redirect('/')
