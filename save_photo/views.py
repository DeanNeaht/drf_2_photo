from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from save_photo.serializers import ImageSerializer
from rest_framework.response import Response


class ImageUploadView(GenericAPIView):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 'OK'})


