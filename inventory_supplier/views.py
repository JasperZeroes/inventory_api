from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer, SupplierSerializer, SupplierDetailSerializer
from .models import Item, Supplier

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        if item.suppliers.exists():
            return Response({'error': 'Cannot delete item associated with a supplier'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return SupplierDetailSerializer
        return SupplierSerializer

    def destroy(self, request, *args, **kwargs):
        supplier = self.get_object()
        # Disassociate items before deleting the supplier
        supplier.items_supplied.clear()
        return super().destroy(request, *args, **kwargs)
