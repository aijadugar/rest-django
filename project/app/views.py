from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


class ReactView(APIView):
    def get(self, request):
        output = [{"employee": output.employee,
                   "department": output.department,
                   } for output in React.objects.all()]
        return Response(output)
        
    def post(self, request):
        serializer = ReactSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)