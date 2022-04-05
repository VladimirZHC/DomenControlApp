# from rest_framework.views import exception_handler


# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)

#     if response is not None:
#         response.data['status_code'] = 500
#         response.data['error'] = 'Internal Server Error'
#         response.data['succes'] = 'False'

#     return response

from django.http import Http404
import logging

from rest_framework.exceptions import  status
from rest_framework.response import Response
from rest_framework.views import exception_handler





def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        return Response(str(exc), status=status.HTTP_404_NOT_FOUND)

  
    response = exception_handler(exc, context)

    
    if response is not None:
        logging.exception('Uncaught Exception', exc_info=exc)
        return Response({'error': 'Internal Server Error', "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    return response