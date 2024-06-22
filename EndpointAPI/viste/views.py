from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize


import json
from django.views.decorators.http import require_http_methods
from EndpointAPI.serializers import OrderSerializer, ProductSerializer
from EndpointAPI.models import Order, Product


@require_http_methods(['GET','POST'])
def filter(request):
    # filtra il valore in base alla data di inizio e fine (le date deveono avere almeno igg di differenza) ritorina l'elenco degli ID associati
    entries=Order.objects.filter()

    if request.method == 'GET':
        if request.GET.get('gte'):
            gte=request.GET.get('gte')
            entries=entries.filter(date__gte=gte)

        if request.GET.get('lte'):
            lte=request.GET.get('lte')
            entries=entries.filter(date__lte=lte)

        if request.GET.get('name') :
            name=request.GET.get('name')
            entries=entries.filter(name__contains=name)

        if request.GET.get('desc') :
            desc=request.GET.get('desc')
            entries=entries.filter(description__contains=desc)


    # # restituisce lista degli id che soddisfano i criteri di filtro
    # response_data={'response':'ok','pyload':list(entr)}
    # return JsonResponse(response_data, safe=False)

    serializer = OrderSerializer(entries, many=True)
    return JsonResponse(serializer.data, safe=False)

@require_http_methods(['GET','POST','DELETE'])
def order(request, id):

    if request.method == 'GET':
        # estrazione voce dettaglio ordine
        entries = Order.objects.get(ID=id)

        #formato risposta
        serializer = OrderSerializer(entries, many=False)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        #estrare i campi da verificare
        fields=Order._meta.fields
        up_data=[]

        #richiama l'oggetto che si vuole modificare
        entries = Order.objects.get(ID=id)

        #Verifica i campi passati con la chiamata POST e li memorizza che devono avere uguale nome a quelli del modello
        for field in fields:
            if request.POST.get(field):
                up_data[field]=request.POST.get(field)
            else:
                #riporta i campi uguali
                up_data[field]=entries[field]

        entry=Order.objects.update_or_create(ID=id,defaults=up_data)
        serializer = OrderSerializer(entry, many=False)
        return JsonResponse(serializer.data, safe=False)


    if request.method == 'DELETE':
        entries = Order.objects.get(ID=id)
        entries.delete()

        response_data={'response':'ok','pyload':id, 'status':'delete'}
        return JsonResponse(response_data, safe=False)
