from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item, Supplier

class ItemTests(APITestCase):

    def test_create_item(self):
        url = reverse('item-list')
        data = {
            'item_id': 1,
            'name': 'Book',
            'description': 'a paperlike structure used for writing',
            'price': '10.00'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Book')

    def test_get_items(self):
        Item.objects.create(item_id=1, name='Book', description='a paperlike structure used for writing', price='10.00')
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Book')

    def test_update_item(self):
        item = Item.objects.create(item_id=1, name='Book', description='a paperlike structure used for writing', price='10.00')
        url = reverse('item-detail', args=[item.item_id])
        data = {
            'item_id': 1,
            'name': 'Updated Book',
            'description': 'A collection of papers',
            'price': '20.00'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.get().name, 'Updated Book')

    def test_delete_item(self):
        item = Item.objects.create(item_id=1, name='Book', description='a paperlike structure used for writing', price='10.00')
        url = reverse('item-detail', args=[item.item_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)


class SupplierTests(APITestCase):

    def test_create_supplier(self):
        url = reverse('supplier-list')
        data = {
            'supplier_id': 1,
            'name': 'Test Supplier',
            'contact_info': 'Test Contact Info'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(Supplier.objects.get().name, 'Test Supplier')

    def test_get_suppliers(self):
        Supplier.objects.create(supplier_id=1, name='Test Supplier', contact_info='Test Contact Info')
        url = reverse('supplier-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Test Supplier')

    def test_update_supplier(self):
        supplier = Supplier.objects.create(supplier_id=1, name='Test Supplier', contact_info='Test Contact Info')
        url = reverse('supplier-detail', args=[supplier.supplier_id])
        data = {
            'supplier_id': 1,
            'name': 'Updated Supplier',
            'contact_info': 'Updated Contact Info'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.get().name, 'Updated Supplier')

    def test_delete_supplier(self):
        supplier = Supplier.objects.create(supplier_id=1, name='Test Supplier', contact_info='Test Contact Info')
        url = reverse('supplier-detail', args=[supplier.supplier_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.count(), 0)
