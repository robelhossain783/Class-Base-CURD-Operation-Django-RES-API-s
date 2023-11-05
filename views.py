from django.shortcuts import render

# Create your views here.
from .models import StudentModel
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentInfo(APIView):
    def get(self, request,pk = None, format= None):
        id = pk
        if id is not None:
            obj = StudentModel.objects.get(id = id)
            serializer = StudentSerializer(obj)
            return Response(serializer.data)
        obj = StudentModel.objects.all()
        serializer = StudentSerializer(obj, many = True)
        return Response(serializer.data)

        
    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    def put(self, request, pk, format = None):
        id = pk
        obj = StudentModel.objects.get(pk = id)
        serializer = StudentSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    def patch(self, request, pk, format = None):
        id = pk
        obj = StudentModel.objects.get(pk = id)
        serializer = StudentSerializer(obj, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self, request, pk, format = None):
        id = pk
        obj = StudentModel.objects.get(pk = id)
        obj.delete()
        return Response({'msg':'Data Delete'})

               