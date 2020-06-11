import cv2

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage

class CarpetImageClassifierAPIView(APIView):

    def post(self, request):
        filename = str(request.data['image'])
        file_obj = request.data['image']
        with default_storage.open('tmp/'+filename, 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        return Response({'h':'h'})