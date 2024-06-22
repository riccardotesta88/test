from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from EndpointAPI.serializers import OrderSerializer, ProductSerializer
from EndpointAPI.models import Order, Product



class ProductItems(viewsets.ReadOnlyModelViewSet):
    '''Api per la gestione degli oggetti in lettura dei prodotti'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.BasePermission]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class OrderItems(viewsets.ModelViewSet):
    '''Api per la gestione degli oggetti del modello associato agli Odini'''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    # Effettua filtro sulle chiamate per estrazione dei dati filtrati
    def get_queryset(self):
        param=self.request.query_params
        print(param)

        if 'gte' in param.keys():
            gte = param['gte']
            self.queryset = self.queryset.filter(date__gte=gte)

        if 'lte' in param.keys():
            lte = param['lte']
            self.queryset = self.queryset.filter(date__lte=lte)

        if 'name' in param.keys():
            name = param['name']
            self.queryset = self.queryset.filter(name__contains=name)

        if 'desc' in param.keys():
            desc = param['desc']
            self.queryset= self.queryset.filter(description__contains=desc)

        return self.queryset

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        ids = request.data.get('ids', [])
        self.queryset.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

