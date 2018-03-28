from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class HelloWorld(APIView):

    def get(self, request):
        return HttpResponse('Hello World Travis setup!')

    def post(self, request):
        return Response(request.data, status=status.HTTP_200_OK)
        