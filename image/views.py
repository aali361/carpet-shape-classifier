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

        img = cv2.imread('tmp/'+filename)

        # add white padding
        WHITE = [255,255,255]
        img= cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_CONSTANT,value=WHITE)

        # convert rgb image into grayscale image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # selecting the threshold which will show binary version of image
        """ Value of pixels is explained below 
        0 means black pixel
        255 means white pixel
        245: Values below 245 means black
        255: Value above 245 means white
        # one can tweak these values for better threshold image
        """
        _, threshold = cv2.threshold(img, 245, 255, cv2.IMREAD_GRAYSCALE)

        # drawing contour on each shape in the image
        contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # loop contour
        contours_sizes= [(cv2.contourArea(cnt), cnt) for cnt in contours]
        biggest_contour = sorted(contours_sizes, key=lambda x: x[0], reverse=True)
        contours = [x[1] for x in biggest_contour]

        for cnt in contours[1:2]:
            approx = cv2.approxPolyDP(cnt, 0.018*cv2.arcLength(cnt, True), True)
            shape = "not detected"
            if len(approx) == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                if  ((float(w)/h)==1):
                    shape = "Square"
                else:
                    shape = "Rectangle"
            else:
                shape = "Circle"

        return Response({'shape': shape})