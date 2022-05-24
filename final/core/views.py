import json
from django.http import JsonResponse
from rest_framework import viewsets
from core.models import Book, Journal
from core.serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import   IsAdminUser
# Create your views here.
class BooksViewSet(viewsets.ViewSet):
    def list(seldf, request):
        queryset = Book.objects.all()
        serializer_class=BookSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
    def get_item(self, request, *args, **kwargs):
        item = Book.objects.filter(id=kwargs.get('id')).first()
        serializer = BookSerializer(item)
        return JsonResponse(serializer.data, safe = False)

class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,)
    
    def create(self, request, *args, **kwargs):
        serializer= BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"created":True}, safe= False)

    def destroy(self,request, *args, **kwargs):
        item = Book.objects.filter(id=kwargs.get('id')).first()
        if item:
            item.delete()
            return JsonResponse({"deleted":True}, safe=False, status=204)
        return JsonResponse({'message': 'item not found'}, status=404)

    def update(self, request, *args, **kwargs):
        item = Book.objects.filter(id=kwargs.get('id')).first()
        if item:
            data = json.loads(self.request.body)
            item.name = data.get('name', item.name)
            item.save()
            serializer = BookSerializer(item)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'message': 'item not found'}, safe=False)


class JournalDetailsViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs): 
        queryset = Journal.objects.all()
        serializer_class=JournalSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)

    def get_item(self, request, *args, **kwargs):
        item = Journal.objects.filter(id=kwargs.get('id')).first()
        serializer = JournalSerializer(item)
        return JsonResponse(serializer.data, safe = False)
class JournalsViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser,)
    
    def create(self, request, *args, **kwargs):
        serializer= JournalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"created":True}, safe= False)

    def destroy(self,request, *args, **kwargs):
        item = Journal.objects.filter(id=kwargs.get('id')).first()
        if item:
            item.delete()
            return JsonResponse({"deleted":True}, safe=False, status=204)
        return JsonResponse({'message': 'item not found'}, status=404)

    def update(self, request, *args, **kwargs):
        item = Journal.objects.filter(id=kwargs.get('id')).first()
        if item:
            data = json.loads(self.request.body)
            item.name = data.get('name', item.name)
            item.save()
            serializer = JournalSerializer(item)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'message': 'item not found'}, safe=False)
