from rest_framework.exceptions import  status
from django.http import  JsonResponse
from rest_framework.response import Response
from domencontrol.settings import DEBUG
from django.conf import settings

class SimpleMiddleWare():
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        data = {
            'error': 'Internal Server Error',
            'success': False,
        }
        response =  self.get_response(request)
        if  response.status_code == status.HTTP_200_OK or response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED   and settings.DEBUG:
            return response
        else:
          return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def process_exception(self, request, exception):
        data = {
            'error': 'Internal Server Error',
            'success': False,
        }
        return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    

