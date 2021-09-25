from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from.models import song

def index(request):
    paginator=Paginator(song.objects.all(),1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)
# Create your views here.
