from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Moto, Opcional

# Create your views here.
def homepage(request):
    title = 'Homepage'
    if request.method == 'GET':
        motos = Moto.objects.all()
        #motos = Moto.objects.all().order_by('nome')

        paginator = Paginator(motos, 6)
        page_number = request.GET.get('page')        
        page_obj = paginator.get_page(page_number)

        search_input = request.GET.get('search') or ''
        if search_input:
            search_input = motos.filter(nome__contains=search_input)
            page_obj = search_input
        return render(request, 'homepage.html',{'motos':motos,'title':title,'page_obj':page_obj,'search_input':search_input})
    

def moto_detalhe(request,id):
    m_nome = Moto.objects.filter(id=id).first()
    title = f'Moto {m_nome.nome} - detalhe'
    if request.method == 'GET':
        moto = Moto.objects.filter(id=id).first()
        return render(request, 'moto_detalhe.html',{'moto':moto,'title':title})
    

def moto_detalhe_pesq(request,opc):
    
    pesquisa = request.GET.get('pesquisa_opcionais')
    motos = Moto.objects.all().filter(opcionais=opc)

    paginator = Paginator(motos, 6)           
    page_obj = paginator.get_page(pesquisa)

    pesq_opcionais = Opcional.objects.filter(id=opc).first()
    return render(request, 'homepage.html',{'motos':motos,'page_obj':page_obj,'pesq_opcionais':pesq_opcionais})


def sobre(request):
    title = 'Sobre'
    return render(request,'sobre.html',{'title':title})

def contato(request):
    title = 'Contato'
    return render(request,'contato.html',{'title':title})
