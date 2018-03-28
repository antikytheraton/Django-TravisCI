from rest_framework.views import APIView
from django.http import HttpResponse


class HelloWorld(APIView):

    def get(self, request):
        return HttpResponse('Hello World Travis setup!')