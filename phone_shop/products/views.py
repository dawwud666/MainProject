from django.shortcuts import render

from .models import *

def product_list(request):
    phones = Phone.objects.all()
    ambassadores = Ambassadores.objects.all()
    Our = Our_supports.objects.all()
    tab = Tab.objects.all()

    context = {
         'phones':phones, 
         'ambassadores':ambassadores,
         'our': Our,
         'tab': tab

    }

    return render(request,'index.html', context )
    

