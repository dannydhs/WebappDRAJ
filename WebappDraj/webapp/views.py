from django.shortcuts import render, render_to_response
from .models import Producto, Produccion
from django.template import RequestContext
from django.http 	 import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives 
from django.contrib.auth import login,logout,authenticate

from django.db.models import Q

def inf_estad_list(request):
	productos = Producto.objects.all()
	producciones = Produccion.objects.order_by('producto').distinct()

	ctx = {
		'productos':productos,
		'producciones':producciones
	}

	return render_to_response('webapp/inf_estad_list.html',ctx,context_instance=RequestContext(request))

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )
        results = Producto.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("webapp/inf_estad_list.html", {
        "results": results,
        "query": query
    })

